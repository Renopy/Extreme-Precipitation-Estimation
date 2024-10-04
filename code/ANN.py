
from tensorflow.keras.metrics import RootMeanSquaredError 
import keras 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow import keras
import numpy
import numpy as np 
import pandas as pd 


#  ________________________________________ Inputs ________________________________________________________


Input_train  = 'D:/train0.csv'
Input_test  = 'D:/test0.csv'


Output_train  = 'D:/train1.csv'
Output_test  = 'D:/test1.csv'


output_model  = 'D:/ANN.keras'

model_name =  'ANN-1'


predictors = [ 'X1'    ,  'X2']
predictant  =  'Y'


model_ann = {   
    'n_neorons' :  [ 64   ] -*6 , 
    'act'       :  [ 'relu'  ] * 6   ,
    'batch'     : 500 , 
    'epoch'     : 12  ,
    'loss_func' :  'mse' , 
    'kernel'    :  "GlorotNormal"  ,
    'optimizer' :   "adam"  ,
    }

# _______________________________________________________________________________________________________

ex_train = pd.read_csv( Input_train  )
ex_test = pd.read_csv(  Input_test )


x_train  = ex_train[predictors].values   
obs_train = ex_train[predictant].values  

x_test = ex_test[predictors].values   
obs_test = ex_test[predictant].values  



n_layer =  len(model_ann['n_neorons'])

Model=Sequential()

Shape_inp = numpy.shape(x_train)


Model.add(Dense(units= model_ann['n_neorons'][0] , 
                input_dim = Shape_inp[1] , kernel_initializer=model_ann[  'kernel' ] 
                , activation=model_ann['act'][0]))

for i in range(1, n_layer):
    Model.add(Dense(units=model_ann['n_neorons'][i],
                    kernel_initializer=model_ann[  'kernel' ] , 
                    activation = model_ann['act'][i] ))
        
Model.add(Dense(units=1,kernel_initializer=model_ann[  'kernel' ] ))

Model.compile(optimizer= model_ann[ "optimizer" ]  , loss= model_ann[ "loss_func" ]  , metrics=[RootMeanSquaredError()])

Model.fit(  x_train ,  obs_train,  batch_size=model_ann[ "batch" ]  ,  epochs=model_ann[ "epoch" ] )

ex_train[model_name]  = Model.predict( x_train )

ex_test[model_name] =   Model.predict(x_test)

cor = np.corrcoef(ex_train[model_name]  ,  ex_test[predictant])
cor_cal = np.corrcoef( ex_train[model_name]  , ex_train[predictant]) 
print( 'test = ' , cor[0,1] ,'train = ' , cor_cal[0,1] )

Model.save(output_model) 


