from flask import render_template
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
# add your google maps api key here
my_google_maps_api_key = 'AIzaSyCLXxaOd3K8TmDd21PYtP8nK_ibDZ4h8Ss'
mapbox_access_token = 'pk.eyJ1IjoiamFja2x1byIsImEiOiJjajNlcnh3MzEwMHZtMzNueGw3NWw5ZXF5In0.fk8k06T96Ml9CLGgKmk81w'
plotly.tools.set_credentials_file(username='sadrik81', api_key='L63ZtbLhPRTl01T9ykKn')

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
def map_hole():
    data = [
        go.Scattermapbox(
            lat=['60','60.12'],
            lon=['30','30'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=14
            ),
            text=['Ямы'],
            
        ),    
        go.Scattermapbox(
            lat=['60.1'],
            lon=['30'],
            mode='markers',
            marker=go.scattermapbox.Marker(
                size=14
            ),
            text=['Трещины'],
            )
    ]

    layout = go.Layout(
        autosize=True,
        hovermode='closest',
        mapbox=go.layout.Mapbox(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=go.layout.mapbox.Center(
                lat=60,
                lon=30
            ),
            pitch=0,
            zoom=6
        ),
    )
    #print (data)
    #fig = go.Figure(data=data, layout=layout)
    #py.iplot(fig, filename='Montreal Mapbox')
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
@app.route('/litter')
def litter():

    #bar = create_plot()
    #return render_template('litter.html', plot=bar)
    bar = map_hole()
    return render_template('litter2.html', plot=bar)
@app.route('/secure')
def secure():

    #bar = map_hole()
    return render_template('secure.html')#, plot=bar)
#транспортная обстановка
@app.route('/road')
def road():
	return render_template('road.html')
@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/social_true')
def home():
	return render_template('social_true.html')
@app.route('/result')
def result():
    user = {'username': 'Miguel'}
    
    return render_template('result.html', title='Home', user=user)
@app.route('/home')
def dash_overview():
	return render_template('olddashboard.html')
@app.route('/')
def dash_overview_2():
	return render_template('olddashboard.html')
