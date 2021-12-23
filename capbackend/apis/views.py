from django.shortcuts import render
from django.http import JsonResponse
from statsmodels.tsa.statespace import sarimax


def apple_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/apple.pkl')
    predictions = loaded.predict(start=80,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'96%','current_price':'$158','predicted_price':'$159', 'labels':['September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$'}
    return JsonResponse(data)

def adidas_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/adidas.pkl')
    predictions = loaded.predict(start=83,end=(85)+3,typ='levels')
    print(len(predictions))
    return JsonResponse({'predictions':list(predictions),'accuracy':'87%','current_price':'$56','predicted_price':'$60'})

def zara_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/zara.pkl')
    predictions = loaded.predict(start=83,end=(85)+3,typ='levels')
    print(predictions)
    return JsonResponse({'predictions':list(predictions),'accuracy':'93%','current_price':'$130','predicted_price':'$127'})

def facebook_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/fb.pkl')
    predictions = loaded.predict(start=83,end=(85)+3,typ='levels')
    print(predictions)
    return JsonResponse({'predictions':list(predictions),'accuracy':'13%','current_price':'$130','predicted_price':'$127'})

def tata_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/tatamotors.pkl')
    predictions = loaded.predict(start=83,end=(85)+3,typ='levels')
    print(predictions)
    return JsonResponse({'predictions':list(predictions),'accuracy':'993%','current_price':'$130','predicted_price':'$127'})