


import pandas as pd 
import numpy as np


Input = r'gnss.csv' 
Output = r'out.xlsx'




df = pd.read_csv(Input)

df['lat'] = df['latitude']

df['long']  = df['longitude']

df[['year', 'month' , 'day hour' ]] = df['report_timestamp'].str.split('-', expand=True)

df[[ 'day' , 'hour' ]] = df['day hour'].str.split(' ', expand=True)

df[['date'  , 'hour']]  = df['report_timestamp'].str.split(' ', expand=True)

for item in [  'year'  ,  'month'  , 'day'] :
    df[item] = np.array(df[item] , dtype= int)

stations = df['station_name'].unique()
Keys = ['station_name'   , 'lat' , 'long' ,   'height_of_station_above_sea_level' , 'year' , 'month' , 'day' ]
out = []
from tqdm import tqdm 
n = len(stations)
for i in tqdm(range( n), desc="Sampling..." , ncols= 100  ,colour='blue'): 
    st = stations[i]
    df_st = df[df['station_name']  == st]
    dates = df_st['date'].unique() 
    for date in dates :
        df_date = df_st[ df_st['date']  == date]
        pwv= df_date['total_column_water_vapour_era5'].sum()
        pwv_mean= df_date['total_column_water_vapour_era5'].mean()
        o = [ ]
        for k in Keys :
            o.append( df_date[k].values[0])
        o.append( pwv)
        o.append( pwv_mean)
        out.append(o)
output = pd.DataFrame( out , columns=Keys + ['pwv' , 'pwv_mean'])

output.to_excel(Output)




