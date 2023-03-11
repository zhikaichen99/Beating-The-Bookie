import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def nba_players():
    # url for a list of nba players
    url = 'https://basketball.realgm.com/nba/players'

    # send a request to the url and get response
    response = requests.get(url)

    # parse content
    soup = BeautifulSoup(response.text, 'html.parser')

    # find table element
    table = soup.find('table', {'class': 'tablesaw'})

    # retrieve headers of the table
    headers = table.find_all('th')
    columns = [th.text for th in headers[1:]]

    # retrieve row data from the table
    data = soup.find('tbody')
    rows = data.findAll('tr')[0:]
    data = []
    for row in rows:
        row_data = []
        for td in row.findAll('td'):
            row_data.append(td.text.strip())
        data.append(row_data[1:])
    df = pd.DataFrame(data, columns = columns)
    return df



def scrape_data_nba(player_name, last_n_games = None):
    # url for the player's game log page
    url = 'https://www.foxsports.com/nba/{}-player-game-log?season=2022&seasonType=reg'.format(player_name)

    # send a request to the url and get response
    response = requests.get(url)

    # parse content
    soup = BeautifulSoup(response.text, 'html.parser')

    # find table element 
    table = soup.find('table', {'class': 'data-table'})

    # retrieve headers of the table
    headers = table.findAll('th', {'class': 'ff-n cell-number pointer'})
    columns = []
    for header in headers:
        columns.append(header.text.strip())

    # retrieve row data from the table
    data = soup.find('tbody', {'class': 'row-data lh-1pt43 fs-14'})
    rows = data.findAll('tr')[0:]
    data = []
    for row in rows:
        row_data = []
        for td in row.findAll('td'):
            row_data.append(td.text.strip())
        data.append(row_data[2:])

    df = pd.DataFrame(data, columns = columns)
    df['3FG'] = df['3FG'].str.split('/').str[0]

    return df[:last_n_games]

def scrape_data_ncaab(player_name, last_n_games = None):

    url = 'https://www.foxsports.com/college-basketball/{}-player-game-log'.format(player_name)

    # send a request to the url and get response
    response = requests.get(url)

    # parse content
    soup = BeautifulSoup(response.text, 'html.parser')

    # find table element 
    table = soup.find('table', {'class': 'data-table'})

    # retrieve headers of the table
    headers = table.findAll('th', {'class': 'ff-n cell-number pointer'})
    columns = []
    for header in headers:
        columns.append(header.text.strip())

    # retrieve row data from the table
    data = soup.find('tbody', {'class': 'row-data lh-1pt43 fs-14'})
    rows = data.findAll('tr')[0:]
    data = []
    for row in rows:
        row_data = []
        for td in row.findAll('td'):
            row_data.append(td.text.strip())
        data.append(row_data[2:])

    df = pd.DataFrame(data, columns = columns)


    return df[:last_n_games]

