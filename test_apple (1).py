import pytest
import os
import pickle
#import modelapple
import pandas as pd
from statsmodels.tsa.arima.model import ARIMAResults
df=pd.read_csv("AAPL.csv", sep=",")
actual_value=df['Close'].iloc[-1]
start= actual_value - 5
end = actual_value + 5

loaded=ARIMAResults.load('apple.pkl')
predictionss = loaded.forecast()
print(predictionss)

#result = mp.score(df)
#print(result)

def check():
  predict_value = predictionss[-1]
  return (predict_value)

def test_pridict():
  assert (check() >= start and check() <= end)
  
test_pridict()