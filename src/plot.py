import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def _setup_plot() -> tuple:
    """Initialize matplotlib figure and axes."""
    plt.style.use('seaborn-v0_8-whitegrid')
    return plt.subplots(figsize=(10, 6))

def _add_scatter(ax, df: pd.DataFrame):
    """Map win/lose colors and plot scatter points."""
    color_map = {'W': '#1f77b4', 'L': '#ff7f0e'}
    colors = df['result'].map(color_map).fillna('gray')
    ax.scatter(df['player_age'], df['age_diff'], c=colors, alpha=0.6, edgecolors='w', s=50)

def plot_career_matches(df: pd.DataFrame):
    """Plot player's age vs age difference with opponent."""
    if df.empty or 'player_age' not in df.columns:
        raise ValueError("DataFrame is empty or missing required columns.")
    
    fig, ax = _setup_plot()
    _add_scatter(ax, df)
    
    ax.axhline(0, color='black', linewidth=1, linestyle='--')
    ax.set_xlabel("Player's Age")
    ax.set_ylabel("Age Difference (Player - Opponent)")
    ax.set_title("Career Matches: Age vs Opponent Age Difference")
    
    plt.tight_layout()
    plt.show()