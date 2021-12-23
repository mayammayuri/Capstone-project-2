import pytest
import os
import pickle
#import modelapple
import pandas as pd
from statsmodels.tsa.arima.model import ARIMAResults
import statsmodels.api as sm
from statsmodels.tsa.statespace import sarimax


df=pd.read_csv("/home/mayuri/Documents/Capstone-project-2/Resources/ADDYY.csv", sep=",")
actual_value=df['Close'].iloc[-1]
start= actual_value - 5
end = actual_value + 5

loaded=sarimax.SARIMAXResultsWrapper.load('/home/mayuri/Desktop/Capstone-project-2/Capstone-project-2/adidas.pkl')
predictionss = loaded.predict(start=len(df),end=(len(df)-1)+3,typ='levels')
print(predictionss)

#result = mp.score(df)
#print(result)

def check():
  predict_value = predictionss[-1]
  return (predict_value)

def test_pridict():
  assert (check() >= start and check() <= end)
  
test_pridict()
