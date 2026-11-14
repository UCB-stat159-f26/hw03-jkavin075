import re
import ast
import requests
import pandas as pd
from datetime import datetime

def _format_name(name: str) -> str:
    """Format name to CamelCase (e.g., 'serena williams' -> 'SerenaWilliams')."""
    return "".join(word.capitalize() for word in name.replace("-", " ").split())

def _extract_variable(js_text: str, var_name: str) -> str:
    """Extract a JavaScript variable definition using regex."""
    match = re.search(rf"var\s+{var_name}\s*=\s*(.*?);", js_text, re.DOTALL)
    if not match:
        raise ValueError(f"Could not find variable {var_name}")
    return match.group(1)

def _calc_age(date_str: str, dob_str: str) -> float:
    """Calculate age in years given YYYYMMDD strings."""
    if not date_str or not dob_str or len(date_str) < 8 or len(dob_str) < 8:
        return None
    d1 = datetime.strptime(date_str[:8], "%Y%m%d")
    d2 = datetime.strptime(dob_str[:8], "%Y%m%d")
    return (d1 - d2).days / 365.25

def _process_matches(matches: list, player_dob: str) -> pd.DataFrame:
    """Process raw match list into a cleaned DataFrame."""
    data = []
    for m in matches:
        match_date, wl = m[0], m[4]
        opp_age_raw = m[16]
        
        player_age = _calc_age(match_date, player_dob)
        if "-" in opp_age_raw or opp_age_raw == "":
            opp_age = None
        elif len(opp_age_raw) == 8 and opp_age_raw.isdigit():
            opp_age = _calc_age(match_date, opp_age_raw)
        else:
            opp_age = float(opp_age_raw)
            
        if player_age and opp_age:
            data.append({"player_age": player_age, "age_diff": player_age - opp_age, "result": wl})
    return pd.DataFrame(data)

def get_player_data(player_name: str) -> pd.DataFrame:
    """Retrieve and process career data for a given tennis player."""
    formatted_name = _format_name(player_name)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    
    career_url = f"https://www.tennisabstract.com/jsmatches/{formatted_name}Career.js"
    resp_career = requests.get(career_url, headers=headers)
    
    if resp_career.status_code != 200 or "var morematchmx" not in resp_career.text:
        raise ValueError(f"Invalid player name or match data not found for: {player_name}")
    
    matches_str = _extract_variable(resp_career.text, "morematchmx")
    matches_list = ast.literal_eval(matches_str)

    bio_url = f"https://www.tennisabstract.com/jsmatches/{formatted_name}.js"
    resp_bio = requests.get(bio_url, headers=headers)
    
    if resp_bio.status_code != 200:
        raise ValueError(f"Could not find biographical data file for: {player_name}")
        
    try:
        player_dob_raw = _extract_variable(resp_bio.text, "dob")
    except ValueError:
        player_dob_raw = _extract_variable(resp_bio.text, "playerdob")
        
    player_dob = player_dob_raw.replace('"', '').replace("'", "")
    
    return _process_matches(matches_list, player_dob)