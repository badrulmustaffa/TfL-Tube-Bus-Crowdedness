import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import json


def tubeline():
    ''' Generating a list of tube stations for Dash Dropdown'''
    data2 = pd.ExcelFile('../data/London-borough.xls')
    zone1lines = pd.read_excel(data2, sheet_name='Zone 1')
    return zone1lines


def figuredata(line):
    '''Importing datasets and creating dataframe to be used in createfigure() by inputing specified tube line'''

    # Importing json file for TfL zone 1 area border.
    # Source:https://stackoverflow.com/questions/31483655/how-to-select-specific-json-element-in-python
    with open('../data/TfL-Zone1-Area.json') as jsonfile:
        geojson = json.load(jsonfile)

    # Importing dataset
    data = pd.ExcelFile('../data/multi-year-station-entry-and-exit-figures.xls')
    data2 = pd.ExcelFile('../data/London-borough.xls')

    # Creating dataframe for chart
    df = pd.read_excel(data, sheet_name='2017 Entry & Exit', skiprows=6)
    station = pd.read_excel(data2, sheet_name='Station')
    zone1lines = pd.read_excel(data2, sheet_name='Zone 1')

    df1 = df.set_index('Station').drop(['Total'])
    df1 = pd.concat([station.rename(columns={'Name': 'Station'}).set_index('Station'), df1], axis=1)

    # Dataframe for stations based on line
    # line = "District"
    onetubeline = pd.DataFrame(index=zone1lines[line].dropna())
    df1 = onetubeline.merge(df1, left_index=True, right_index=True, )
    df1 = df1.reset_index().rename(columns={'index': 'Station'})

    return df1, geojson


def createfigure(line):
    '''Generating figure by inputing the specified line from the Dash App'''
    df1, geojson = figuredata(line)

    # Creating scattermapbox
    mapbox_access_token = "pk.eyJ1IjoiYmFkcnVsbXVzdGFmZmEiLCJhIjoiY2ttMzE1cXgzNGJ0dzJ1bnc0Z3hkZnBpbSJ9." \
                          "GEDuGnidtzWvTiXPCGIX4w"
    fig = px.scatter_mapbox(df1, lat="Latitude", lon="Longitude",
                            size="million", size_max=15,  # zoom=10,
                            text=df1['Station'],
                            # title="Zone 1 TfL tube station yearly entry and exit based on line",
                            labels={'million': 'No. of entry and exit yearly (in millions)'}
                            )

    # Adding Zone 1 border using mapbox layout. Adapted from:
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10},
                      autosize=True,
                      showlegend=True,
                      mapbox=go.layout.Mapbox(
                          dict(accesstoken=mapbox_access_token),
                          zoom=11, center={"lat": 51.5087, "lon": -0.1346},
                          layers=[{
                              'sourcetype': 'geojson',
                              'source': geojson,
                              'type': 'line',
                              'name': "Zone 1"
                          }]
                      )
                      )
    return fig


def AreaList(mean):
    ''' Generating a list of tube stations for Dash Dropdown'''
    data = pd.ExcelFile('../data/Tube_and_Bus_Route_Stops.xls')
    if 'Bus' in mean:
        sheet = 'Bus Regions'
    else:
        sheet = 'Tube Regions'
    area_list = pd.read_excel(data, sheet_name=sheet, skiprows=1)
    return area_list

def CreateBorders(mean):
    # Setting the json for appropriate mean and opening the file
    if 'Bus' in mean:
        json_file = 'data/bus_region_map.json'
    else:
        json_file = 'data/tube_region_map.json'
    with open(json_file) as jsonfile:
        geojson = json.load(jsonfile)

    # Create dataframe from dataset
    data = pd.ExcelFile('')
    data2 = pd.ExcelFile('data/London-borough.xls')
    df = pd.read_excel(data, sheet_name='2017 Entry & Exit', skiprows=6)

    # Creating dataframe for borough stations
    boroughlist = pd.read_excel(data2, sheet_name='Borough').set_index("Borough")

    df1 = df['Borough'].value_counts().reset_index(). \
        rename(columns={'index': 'Borough', 'Borough': 'Frequency'}).set_index("Borough")
    df1 = pd.concat([boroughlist, df1], axis=1).reset_index().fillna(0)

    # Creating a cheropleth graph for borough
    fig = px.choropleth_mapbox(df1, geojson=geojson, locations='Borough',
                               color='Frequency', range_color=(0, 31),
                               color_continuous_scale="Viridis",
                               mapbox_style="carto-positron",
                               featureidkey="properties.id",
                               zoom=8.2, center={"lat": 51.5074, "lon": -0.1},
                               width=600, opacity=0.6,
                               title="TfL tube stations in 2017 based on Borough",
                               labels={'Frequency': 'No. of station'})

    return fig
