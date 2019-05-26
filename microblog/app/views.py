﻿from flask import render_template, Flask
from app import app
import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
import plotly.plotly as py
from plotly.graph_objs import *

import numpy as np
import requests
import copy
import googlemaps
import plotly.plotly as py
import plotly.graph_objs as go
from PIL import ImageTk, Image
import os
import webbrowser
import twitter
import json
import time
import nltk
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from nltk.stem.snowball import SnowballStemmer
import string
from nltk.stem.porter import PorterStemmer
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
from gensim import corpora, models, similarities 
import gensim
import os 
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.manifold import MDS
from sklearn.decomposition import NMF
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
from collections import Counter
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
# implement the default mpl key bindings
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
# add your google maps api key here

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

my_google_maps_api_key = 'AIzaSyCLXxaOd3K8TmDd21PYtP8nK_ibDZ4h8Ss'
mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'
plotly.tools.set_credentials_file(username='sadrik81', api_key='L63ZtbLhPRTl01T9ykKn')
def callback():
    #----------------------------------------------------------------------обращение к API Twitter


    CONSUMER_KEY = '3NTp6bVmDdLPXo8bjW4syW7uk'
    CONSUMER_SECRET = 'GkSBgJTExl54xmkOJxA2M0LFnhpyWwAuYDs4jRUEo8nxKz1H8S'
    OAUTH_TOKEN = '2308267840-slR7ovWLIIJtXeMlwXlAfzauWkkpGHSMm9cm6ct'
    OAUTH_TOKEN_SECRET = 'pGjYDpoRI2Zu4W5b5yLBGOXYQAOOGeBoH0CHt3oBZdVvt'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    tweet=twitter_api.search.tweets(q='Санкт-Петербург', count="100")
    p = json.dumps(tweet)
    res2 = json.loads(p)
    print (u'Получено сообщений: ',len(res2['statuses']))
#callback()
def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/litter')
def litter():
    posts = [
    {
        'author': {'username': 'Очень грязно'},
        'body': '72'
    },
    {
        'author': {'username': 'Грязно'},
        'body': '88'
    }, 
    {
        'author': {'username': 'Чисто'},
        'body': '334'
    }
    ]
    #bar = create_plot()
    #return render_template('litter.html', plot=bar)
    #bar = map_hole()
    return render_template('litter2.html',  posts=posts)
@app.route('/secure')
def secure():


    #bar = map_hole()
    return render_template('secure.html')#, plot=bar)
#транспортная обстановка
@app.route('/road')
def road():
    posts = [
    {
        'author': {'username': 'Ямы'},
        'body': '1'
    },
    {
        'author': {'username': 'Трещины'},
        'body': '142'
    }, 
    {
        'author': {'username': 'Повреждения разметки'},
        'body': '217'
    }
    ]
    
    return render_template('road.html', posts=posts)
@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/social_true')
def home():
	return render_template('social_true.html')
@app.route('/result')
def result():
    user = {'username': 'Эльдар Рязанов'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Ипполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    #return render_template('index.html', title='Home', user=user, posts=posts)
    
    return render_template('social_true.html', title='Home', user=user, posts=posts)
@app.route('/home')
def dash_overview():
	return render_template('olddashboard.html')
	
@app.route('/')
def dash_overview():
	return render_template('olddashboard.html')


if __name__ == '__main__':

    app.run(debug=False,threaded = True, host='0.0.0.0', port=80)