import pytest
import pandas as pd
from hw03-jkavin075.data import _process_matches

# Mock Data
MOCK_FEMALE_JS = [
    ["19951030", "Canadian Open", "Carpet", "W", "L", "", "", "WC", "Q1", "6-1 6-1", "3", "Anne Miller", "149", "7", "", "R", "19770119", "", "USA", "0", "", "", "", "", "", "", "1995-013"],
    ["19970307", "Indian Wells", "Hard", "W", "L", "", "", "WC", "Q1", "6-4 6-0", "3", "Alexia", "87", "", "", "R", "19700503", "", "FRA", "0", "", "", "", "", "", "", "1997-006"]
]

MOCK_MALE_JS = [
    ["20010910", "Spain F10", "Hard", "S", "L", "", "", "WC", "R32", "2-6 7-5 6-2", "3", "Guillermo", "731", "", "", "R", "22.26", "", "ESP", "0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "2001-002", "", "1", "1"],
    ["20010917", "Seville CH", "Clay", "C", "W", "", "", "WC", "R32", "6-4 6-4", "3", "Israel", "751", "", "Q", "U", "18.75", "", "ESP", "0", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "2001-015", "", "1", "1"]
]

PLAYER_DOB = "19810926" # Serena's DOB for test context

def test_female_player_processing():
    df = _process_matches(MOCK_FEMALE_JS, PLAYER_DOB)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert "player_age" in df.columns
    assert "age_diff" in df.columns
    # Check age calculation logic (1995 - 1981 = ~14 years)
    assert 13.5 < df.iloc[0]['player_age'] < 14.5 

def test_male_player_processing():
    df = _process_matches(MOCK_MALE_JS, PLAYER_DOB)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2
    assert df.iloc[0]['result'] == 'L'
    assert df.iloc[1]['result'] == 'W'