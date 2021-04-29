import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import json


def AreaList(mean):
    """''' Generating a list of tube stations for Dash Dropdown '''"""
    data = pd.ExcelFile('../data/Tube_and_Bus_Route_Stops.xls')
    if 'Bus' in mean:
        sheet = 'Bus Regions'
    else:
        sheet = 'Tube Regions'
    area_list = pd.read_excel(data, sheet_name=sheet, skiprows=1)
    return area_list


def CreateBorders(mean, start, end):
    """ Inserting the transportation mode as mean, start point and end point and returning the """
    # Setting the json for appropriate mean and opening the file
    if 'Bus' in mean:
        json_file = '../data/bus_region_map.json'
    else:
        json_file = '../data/tube_region_map.json'
    with open(json_file) as jsonfile:
        geojson = json.load(jsonfile)

    mapbox_access_token = "pk.eyJ1IjoiYmFkcnVsbXVzdGFmZmEiLCJhIjoiY2ttMzE1cXgzNGJ0dzJ1bnc0Z3hkZnBpbSJ9." \
                          "GEDuGnidtzWvTiXPCGIX4w"

    if start is None:
        start = ''

    if end is None:
        end = ''

    # Create dataframe from dataset
    df = AreaList(mean)[{'Name'}].set_index('Name')
    df["Status"] = np.nan
    df.loc[start, 'Status'] = 'Start'
    df.loc[end, 'Status'] = 'End'
    df = df.reset_index().dropna()

    fig = px.choropleth_mapbox(df, geojson=geojson, locations='Name',
                               color='Status',
                               color_discrete_map={'Start': 'blue', 'End': 'red'},
                               mapbox_style="open-street-map",
                               featureidkey="properties.id",
                               opacity=1,
                               labels={'Status': 'Legend'})

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10},
                      autosize=True,
                      showlegend=False,
                      mapbox=go.layout.Mapbox(
                          dict(accesstoken=mapbox_access_token),
                          zoom=11, center={"lat": 51.5087, "lon": -0.1346},
                          layers=[{
                              'sourcetype': 'geojson',
                              'source': geojson,
                              'type': 'line',
                          }]
                      ),
                      mapbox_style="streets"
                      )
    return fig
