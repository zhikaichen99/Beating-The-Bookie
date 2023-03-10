# Importing necessary libraries
import pandas as pd
from utils.scraper import scrape_data_nba
from utils.probability import player_over_probability
import datetime

# Thresholds for different categories of stats
POINTS_THRESHOLDS = [5, 10, 15, 20, 25]
ASSISTS_THRESHOLDS = [3, 5, 7, 10, 13]
REBOUNDS_THRESHOLDS = [3, 5, 7, 10, 13]
THREES_THRESHOLDS = [1, 2, 3, 4, 5]

# Number of last games to consider for analysis
LAST_N_GAMES = 25

# Players to consider for analysis
PLAYERS_LIST = ['anthony-edwards']

# Defining main function
def nba():
    df = pd.DataFrame()
    for player_name in PLAYERS_LIST:
        player_df = scrape_data_nba(player_name, LAST_N_GAMES)
        player_df = player_df.astype({'PTS': int, 'AST': int, 'REB': int, '3FG': int})
        player_name = player_name.replace('-', ' ').title()
        print(f"Created DataFrame for {player_name}")

        # Looping over each category and threshold to calculate the probability
        for category, thresholds in zip(['PTS', 'AST', 'REB', '3FG'],
                                        [POINTS_THRESHOLDS, ASSISTS_THRESHOLDS, REBOUNDS_THRESHOLDS, THREES_THRESHOLDS]):
            player_list, prop_list, probability_list, last_25_list, average_list = [], [], [], [], []
            for threshold in thresholds:
                probability = player_over_probability(category, threshold, player_df)
                last_25 = player_df[player_df[category] >= threshold]
                count_last_25 = last_25.shape[0]
                average = player_df[category].mean()

                # Checking if the probability of going over the threshold is higher than 80%
                if (0.80 <= probability <= 0.95):
                    player_list.append(player_name)
                    prop_list.append(f"{threshold} {category}")
                    probability_list.append(probability)
                    last_25_list.append(count_last_25)
                    average_list.append(average)
            data = {'Player': player_list, 'Prop': prop_list, 'Probability': probability_list,
                    'Last_25': last_25_list, 'Average_Last_25': average_list}
            df_results = pd.DataFrame(data)
            df = pd.concat([df, df_results])

    df.reset_index(drop=True, inplace=True)
    print(df)

    # Saving the results to a csv file with today's date
    today = datetime.date.today()
    df.to_csv(f"{today}-nba-bets.csv")




if __name__ == '__main__':
    nba()
