from flask import render_template
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
my_google_maps_api_key = 'AIzaSyCLXxaOd3K8TmDd21PYtP8nK_ibDZ4h8Ss'
mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'
plotly.tools.set_credentials_file(username='sadrik81', api_key='L63ZtbLhPRTl01T9ykKn')

def callback(name):
    #----------------------------------------------------------------------обращение к API Twitter


    CONSUMER_KEY = '3NTp6bVmDdLPXo8bjW4syW7uk'
    CONSUMER_SECRET = 'GkSBgJTExl54xmkOJxA2M0LFnhpyWwAuYDs4jRUEo8nxKz1H8S'
    OAUTH_TOKEN = '2308267840-slR7ovWLIIJtXeMlwXlAfzauWkkpGHSMm9cm6ct'
    OAUTH_TOKEN_SECRET = 'pGjYDpoRI2Zu4W5b5yLBGOXYQAOOGeBoH0CHt3oBZdVvt'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    tweet=twitter_api.search.tweets(q=name, count="15")
    p = json.dumps(tweet)
    res2 = json.loads(p)
    j=0
    post=[]
    lang=[]
    while j<len(res2['statuses']):
        dict1={'author': {'username': (res2['statuses'][j]['user']['name'])},
            'body': res2['statuses'][j]['text'].encode('utf-8')}
        #print (u'Получено сообщений: ',len(res2['statuses']))
        lang.append(res2['statuses'][j]['user']['lang'])
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
    t =list( Counter(lang).keys())
    s = list(Counter(lang).values())
    print (t,s)


callback('Saint-Petersburg')
