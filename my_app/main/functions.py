import pandas as pd

def ConvertNavigationVariables(mean, start, end):
    data = pd.ExcelFile('../data/Tube_and_Bus_Route_Stops.xls')
    sheet = 'Bus Regions'
    mean_map = 'bus_map'
    if 'Tube' in  mean:
        sheet = 'Tube Regions'
        mean_map = 'tube_map'
    df = pd.read_excel(data, sheet_name=sheet, skiprows=1)

    if start is None:
        start = ''
    if end is None:
        end = ''

    # Create dataframe from dataset
    df = df[{'Name', 'Number'}].set_index('Name')
    start_number = df.loc[start, 'Number']
    end_number = df.loc[end, 'Number']

    return mean_map, start_number, end_number
