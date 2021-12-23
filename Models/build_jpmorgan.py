##!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
import os


# In[2]:


# get_ipython().system('pip install statsmodels ')


# In[4]:


import pandas as pd
df=pd.read_csv("F:\sem 7\project\Capstone-project-2\Resources\JPM.csv", sep=",")
df


# In[5]:


#plt.figure()
#lag_plot(df['Open'])
#plt.title('Apple Stock - Autocorrelation plot with lag = 3')
#plt.show()


# In[6]:


#plt.plot(df["Date"], df["Close"])
#plt.xticks(np.arange(0,1259, 200), df['Date'][0:1259:200])
#plt.title("Apple stock price over time")
#plt.xlabel("time")
#plt.ylabel("price")
#plt.show()


# In[7]:

from statsmodels.tsa.statespace.sarimax import SARIMAX

train_data, test_data = df[0:int(len(df)*0.7)], df[int(len(df)*0.7):]
training_data = train_data['Close'].values
test_data = test_data['Close'].values
history = [x for x in training_data]
testing_predictions= [x for x in test_data]

model_predictions = []
N_test_observations = len(test_data)
models = []
for time_point in range(N_test_observations):
    model = SARIMAX(history, order=(0,1,0),seasonal_order=(2,1,0,4))
    model_test = SARIMAX(history, order=(0,1,0),seasonal_order=(2,1,0,4))
    model_fit = model.fit()
    model_test_fit=model_test.fit()
    #fc,se,conf = model_fit.forecast()
    output = model_fit.forecast()
    yhat = output[0]
    models.append(model_fit)
    model_predictions.append(int(yhat))
    true_test_value = test_data[time_point]
    history.append(true_test_value)
MSE_error = mean_squared_error(test_data, model_predictions)
#print('Testing Mean Squared Error is {}'.format(MSE_error))


# In[ ]:


import pickle

from statsmodels.tsa.arima_model import ARIMAResults
model_test_fit.save("JPMorgan.pkl") 