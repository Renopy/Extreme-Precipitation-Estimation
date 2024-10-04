


import h5py 
import pandas as pd
import numpy as np 
import xarray 




Folder = "D:/Projects/precipitation_AUS/dataset/0024/"
files = os.listdir(Folder)
hdfs = []

for file in files :
    hdf = h5py.File(Folder + file , 'r+')
    hdfs.append( hdf)

needed_keys = [ 'NAME'  , 'LATITUDE' , 'LONGITUDE' ,  'YEAR'  , 'MONTH'   ,  'DAY'  , 'PRCP'  , 
               'LSTM_RA_3(-4)','LSTM_RA_3(-3)',  'LSTM_RA_3(-2)','LSTM_RA_3(-1)', 'LSTM_RA_3'  ,  'LSTM_RA_2'  , 'LSTM_RA_1'  ,
      'LSTM_RA_0(-4)' , 'LSTM_RA_0(-3)'  , 'LSTM_RA_0(-2)' , 
      'LSTM_RA_0(-1)' , 'LSTM_RA_0' , 'CAL_P'   ,'PDIR' , 'ERA5_tp'  , 'CNN_RA_(3,3)',
 'CNN_RA_(5,5)',
 'CNN_RA_(7,7)',
 'CNN_RA_C_(3,3)',
 'CNN_RA_C_(5,5)',
 'CNN_RA_C_(7,7)',
 'CNN_RA_C_[-1](7,7)',
 'CNN_RA_C_[-2](7,7)',
 'CNN_RA_C_[-3](7,7)'
] 

DF = pd.DataFrame()
for k in needed_keys :
    DF[k] = np.array(hdfs[0][k])

