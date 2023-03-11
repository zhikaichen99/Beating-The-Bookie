from flask import Flask, render_template, request
import pandas as pd

from utils.sports_bets import basketball
from utils.scraper import nba_players

import streamlit as st
import numpy as np


st.set_page_config(
    page_title="Beating The Bookie", page_icon="📊", initial_sidebar_state="expanded"
)

st.write(
    """
# Beating The Bookie
Using stat and probability for sports betting props .
"""
)






if __name__ == '__main__':

    with st.sidebar:

        sport = st.selectbox(
        'Which sport do you want to look at',
        ['NBA', 'NCAA', 'NBL'])

        players = st.multiselect(
        'Which player(s) do you want to look at',
        nba_players()['Player'].tolist()
        )

        stats = st.multiselect(
            'Which stat(s) do you want to look at',
            ['Points', 'Assists', 'Rebounds', 'Threes'])

            
        
        if 'Points' in stats:
            points_thresholds = st.multiselect(
                'Points',
                [num/2 for num in range(0,61)]    
            )
        
        if 'Assists' in stats:
            assists_thresholds = st.multiselect(
                'Assists',
                [num/2 for num in range(0,41)]
            )
        
        if 'Rebounds' in stats:
            rebounds_thresholds = st.multiselect(
                'Rebounds',
                [num/2 for num in range(0,41)]
            )
        
        if 'Threes' in stats:
            threes_thresholds = st.multiselect(
                'Threes',
                [num/2 for num in range(0,11)]
            )

    if len(stats) != 0:

        last_n_games = 25

        player_list = []
        for player in players:
            player = player.replace(" ", "-").lower()
            player_list.append(player)

        bets_df = basketball(player_list, last_n_games, points_thresholds, assists_thresholds, rebounds_thresholds, threes_thresholds)

        st.dataframe(bets_df, use_container_width = True)
   










