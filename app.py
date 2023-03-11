from flask import Flask, render_template, request
import pandas as pd
from utils.scraper import scrape_data_nba
from utils.probability import player_over_probability

import streamlit as st
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

# Thresholds for different categories of stats
POINTS_THRESHOLDS = [5, 10, 15, 20, 25]
ASSISTS_THRESHOLDS = [3, 5, 7, 10, 13]
REBOUNDS_THRESHOLDS = [3, 5, 7, 10, 13]
THREES_THRESHOLDS = [1, 2, 3, 4, 5]

# Number of last games to consider for analysis
LAST_N_GAMES = 25

# Players to consider for analysis
PLAYERS_LIST = ['anthony-edwards']

NCAA_PLAYERS_LIST = ['andrew-funk', 'seth-lundy', 'jalen-pickett', 'camren-wynter',
                     'chase-audige', 'ty-berry', 'boo-buie', 'matthew-nicholson',
                     'taylor-hendricks', 'ithiel-horton', 'darius-johnson', 'cj-kelly',
                     'kendric-davis', 'elijah-mccadden',
                     'tyrese-proctor', 'jeremy-roach', 'jordan-miller', 'norchard-omier',
                     'nijel-pack', 'wooga-poplar', 'isaiah-wong', 'jaren-holmes', 'gabe-kalscheur',
                     'tre-king', 'gradey-dick', 'jalen-wilson', 'isiah-dasher', 'gabe-mcglothan',
                     'qua-grant', 'donte-powers', 'donald-carey', 'hakim-hart',
                     'julian-reese', 'donta-scott','jahmir-young', 'trey-galloway',
                     'miller-kopp', 'race-thompson', 'jermaine-couisnard', 'will-richardson',
                     'amari-bailey', 'tyger-campbell']

data= pd.read_csv('df_sample_data.csv', index_col=0) 




