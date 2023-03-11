from flask import Flask, render_template, request
import pandas as pd
from utils.scraper import scrape_data_nba
from utils.probability import player_over_probability

import streamlit as st
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

data= pd.read_csv('df_sample_data.csv', index_col=0) 




