# Importing necessary libraries
import pandas as pd
from utils.scraper import scrape_data_nba, scrape_data_ncaab
from utils.probability import player_over_probability
import datetime


# Defining main function
def basketball(players_list, last_n_games, points_thresholds, assists_thresholds, rebounds_thresholds, threes_threshold):
    df = pd.DataFrame()
    for player_name in players_list:
        try:
            player_df = scrape_data_nba(player_name, last_n_games)
            player_df = player_df.astype({'PTS': int, 'AST': int, 'REB': int, '3FG': int})
            player_name = player_name.replace('-', ' ').title()
            print(f"Created DataFrame for {player_name}")

            # Looping over each category and threshold to calculate the probability
            for category, thresholds in zip(['PTS', 'AST', 'REB', '3FG'],
                                            [points_thresholds, assists_thresholds, rebounds_thresholds, threes_threshold]):
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
        except Exception as e:
            # print the error message and continue to the next item
            print("Error for : {}".format(player_name))
            continue

    df.reset_index(drop=True, inplace=True)

    # Saving the results to a csv file with today's date
    #today = datetime.date.today()
    #df.to_csv(f"{today}-nba-bets.csv")

    return df

# def ncaab(players_list):
#     df = pd.DataFrame()
#     for player_name in players_list:
#         try:
#             player_df = scrape_data_ncaab(player_name, last_n_games)
#             player_df = player_df.astype({'PTS': int, 'AST': int, 'REB': int})
#             player_name = player_name.replace('-', ' ').title()
#             print(f"Created DataFrame for {player_name}")

#             # Looping over each category and threshold to calculate the probability
#             for category, thresholds in zip(['PTS', 'AST', 'REB'],
#                                             [POINTS_THRESHOLDS, ASSISTS_THRESHOLDS, REBOUNDS_THRESHOLDS]):
#                 player_list, prop_list, probability_list, last_25_list, average_list = [], [], [], [], []
#                 for threshold in thresholds:
#                     probability = player_over_probability(category, threshold, player_df)
#                     last_25 = player_df[player_df[category] >= threshold]
#                     count_last_25 = last_25.shape[0]
#                     average = player_df[category].mean()

#                     # Checking if the probability of going over the threshold is higher than 80%
#                     if (0.80 <= probability <= 0.95):
#                         player_list.append(player_name)
#                         prop_list.append(f"{threshold} {category}")
#                         probability_list.append(probability)
#                         last_25_list.append(count_last_25)
#                         average_list.append(average)
#                 data = {'Player': player_list, 'Prop': prop_list, 'Probability': probability_list,
#                         'Last_25': last_25_list, 'Average_Last_25': average_list}
#                 df_results = pd.DataFrame(data)
#                 df = pd.concat([df, df_results])
#         except Exception as e: 
#             # print the error message and continue to the next item
#             print("Error for : {}".format(player_name))
#             continue
    
#     df.reset_index(drop=True, inplace=True)

#     # Saving the results to a csv file with today's date
#     today = datetime.date.today()
#     df.to_csv(f"{today}-ncaa-bets.csv")


# if __name__ == '__main__':
#     ncaab()
