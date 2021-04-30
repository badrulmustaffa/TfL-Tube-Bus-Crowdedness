import plotly.express as px
import pandas as pd

# data = pd.read_excel('data/multi-year-station-entry-and-exit-figures-dataset-with-zone1.xlsx',
#                      sheet_name='2017 Entry & Exit (Zone 1)', skiprows=6)
from my_app.main.functions import dataprocessor
mean = 'Bus'
start = 'Bayswater, Notting Hill Gate'
end = 'Tower Hill'

df, a, b = dataprocessor(mean, start, end)

# wide_df = px.data.medals_wide()

fig = px.bar(df, x="Group Alphabet", y="total", title="Wide-Form Input")
fig.show()
