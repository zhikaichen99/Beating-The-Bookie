import pandas as pd
import streamlit as st

from utils.sports_bets import basketball
from utils.scraper import nba_players

# Set page title, icon, and initial sidebar state
st.set_page_config(
    page_title="Beating The Bookie",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# Set theme to "light"
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_theme('light')

# Add a title and description to the app
st.write(
    """
    # Beating The Bookie
    Using stat and probability for sports betting props.
    """
)

# Create a sidebar with selection boxes for sport, player, and stats
with st.sidebar:
    # Sport selection
    sport = st.selectbox(
        'Select a sport:',
        ['NBA', 'NCAA', 'NBL']
    )

    # Player selection
    players = st.multiselect(
        'Select player(s):',
        nba_players()['Player'].tolist()
    )

    # Stat selection
    stats = st.multiselect(
        'Select stat(s):',
        ['Points', 'Assists', 'Rebounds', 'Threes']
    )

    # Show numeric input fields for each selected stat
    for stat in stats:
        if stat == 'Points':
            points_thresholds = st.slider(
                'Select a range of points:',
                min_value=0.0,
                max_value=30.0,
                step=0.5,
                value=(0.0, 30.0)
            )

        elif stat == 'Assists':
            assists_thresholds = st.slider(
                'Select a range of assists:',
                min_value=0.0,
                max_value=20.0,
                step=0.5,
                value=(0.0, 20.0)
            )

        elif stat == 'Rebounds':
            rebounds_thresholds = st.slider(
                'Select a range of rebounds:',
                min_value=0.0,
                max_value=20.0,
                step=0.5,
                value=(0.0, 20.0)
            )

        elif stat == 'Threes':
            threes_thresholds = st.slider(
                'Select a range of threes:',
                min_value=0.0,
                max_value=5.0,
                step=0.5,
                value=(0.0, 5.0)
            )

# Display the results in a data frame
if len(stats) != 0:
    last_n_games = 25

    player_list = []
    for player in players:
        player = player.replace(" ", "-").lower()
        player_list.append(player)

    bets_df = basketball(
        player_list,
        last_n_games,
        points_thresholds,
        assists_thresholds,
        rebounds_thresholds,
        threes_thresholds
    )

    st.write('## Betting Proposals')
    st.dataframe(bets_df)


