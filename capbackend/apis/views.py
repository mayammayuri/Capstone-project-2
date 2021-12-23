from django.shortcuts import render
from django.http import JsonResponse
from statsmodels.tsa.statespace import sarimax
import datetime
# Create your views here.
def apple_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/apple.pkl')
    predictions = loaded.predict(start=83,end=(85)+3,typ='levels')
    print(predictions)
    return JsonResponse({'predictions':list(predictions),'accuracy':'96%','current_price':'$158','predicted_price':'$159'})

def adidas_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/adidas.pkl')
    predictions = loaded.predict()
    print(len(predictions))
    return JsonResponse({'predictions':list(predictions),'accuracy':'87%','current_price':'$56','predicted_price':'$60'})

def zara_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/zara.pkl')
    predictions = loaded.forecast()
    print(predictions)
    return JsonResponse({'predictions':list(predictions),'accuracy':'93%','current_price':'$130','predicted_price':'$127'})

def facebook_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/fb.pkl')
    predictions = loaded.forecast()
    print(predictions)
    return JsonResponse({'predictions':list(predictions),'accuracy':'13%','current_price':'$130','predicted_price':'$127'})

def tata_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/tatamotors.pkl')
    predictions = loaded.forecast()
    print(predictions)
    return JsonResponse({'predictions':list(predictions),'accuracy':'993%','current_price':'$130','predicted_price':'$127'})