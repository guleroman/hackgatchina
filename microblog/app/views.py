from flask import render_template, Flask

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json
import plotly.plotly as py
from plotly.graph_objs import *


import plotly.graph_objs as go
from PIL import Image
import os

import twitter

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
# add your google maps api key here
my_google_maps_api_key = ''
mapbox_access_token = 'pk..'
plotly.tools.set_credentials_file(username='', api_key='')
def callback():
    #----------------------------------------------------------------------обращение к API Twitter


    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
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
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    tweet=twitter_api.search.tweets(q='Gatchina', count="15")
    p = json.dumps(tweet)
    res2 = json.loads(p)
    j=0
    post=[]
    while j<len(res2['statuses']):
        dict1={'author': {'username': (res2['statuses'][j]['user']['name'])},
            'body': res2['statuses'][j]['text'],
               'date':res2['statuses'][j]['created_at'],
               'lang': res2['statuses'][j]['user']['lang'],
               'count': res2['statuses'][j]['user']['followers_count'],
               'status': res2['statuses'][j]['user']['statuses_count']}
        #print (u'Получено сообщений: ',len(res2['statuses']))
        """
        print (res2['statuses'][j]['text'].encode('utf-8'))
        print (str(res2['statuses'][j]['user']['name']).encode('utf-8'))
        print (res2['statuses'][j]['created_at'])
        print (res2['statuses'][j]['user']['followers_count'])
        print (res2['statuses'][j]['user']['lang'])
        print (res2['statuses'][j]['user']['statuses_count'])
        """
        post.append(dict1)
        j=j+1
    return render_template('social_true.html', title='Home', posts=post)
@app.route('/home')
def dash_overview():
	return render_template('olddashboard.html')
@app.route('/admin')
def admin():
	return render_template('admin.html')
@app.route('/')
def dash_overview_2():
	return render_template('olddashboard.html')

if __name__ == '__main__':

    app.run(debug=False,threaded = True, host='0.0.0.0', port=80)
