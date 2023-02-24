from flask import Flask, render_template, request
import pandas as pd
from utils.scraper import scrape_data
from utils.probability import player_over_probability

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    player_name = request.form['player_name']
    threshold = int(request.form['threshold'])
    stat = request.form['stat']
    last_n_games = int(request.form['last_n_games'])

    df = scrape_data(player_name, last_n_games)
    probability = player_over_probability(stat, threshold, df)

    return render_template('index.html', prediction_text='The probability of {} getting over {} {} is {:.2f}%'.format(player_name, threshold, stat, probability*100))

if __name__ == "__main__":
    app.run(debug=True)


