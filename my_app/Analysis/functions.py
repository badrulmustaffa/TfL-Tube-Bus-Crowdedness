import plotly.express as px
import pandas as pd

# data = pd.read_excel('data/multi-year-station-entry-and-exit-figures-dataset-with-zone1.xlsx',
#                      sheet_name='2017 Entry & Exit (Zone 1)', skiprows=6)
data = pd.read_excel('../data/multi-year-station-entry-and-exit-figures.xls',
                     sheet_name='2017 Entry & Exit (Zone 1)', skiprows=6)

df = pd.DataFrame(data)
df1 = pd.DataFrame(index=range(23), columns=['total']).fillna(0)
df2 = df['Group Alphabet'].drop_duplicates().dropna().reset_index()

for x, poo in df1.iterrows():
    for y, lines in df.iterrows():
        if x == lines['Group Number']:
            poo['total'] += lines['million']

df3 = pd.concat([df1, df2['Group Alphabet']], axis=1, join='inner')

# wide_df = px.data.medals_wide()

fig = px.bar(df3, x="Group Alphabet", y="total", title="Wide-Form Input")
fig.show()
