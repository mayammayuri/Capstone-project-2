from django.shortcuts import render
from django.http import JsonResponse
from statsmodels.tsa.statespace import sarimax


def apple_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/apple.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def adidas_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/adidas.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    data={'predictions':list(predictions),'accuracy':'96.45%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Adidas/ADDYY', 'current_price':'$175.13', 'predicted_price':'$170.91', 'up_down_current':'fas fa-arrow-down text-failure', 'up_down_predicted':'fas fa-arrow-down text-failure', 'up_down_current_since':'$2.66', 'predicted_current':'2.47%'}
    return JsonResponse(data)

def zara_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/zara.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    data={'predictions':list(predictions),'accuracy':'92.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Zara/ZARA', 'current_price':'$40.12', 'predicted_price':'$45.28', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$8.5', 'predicted_current':'11.40%'}
    return JsonResponse(data)

def facebook_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/fb.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'95.45%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Facebook/FB', 'current_price':'$318.37', 'predicted_price':'$345.66', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6', 'predicted_current':'7.90%'}
    return JsonResponse(data)

def tata_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/tatamotors.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'88.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'Rs.', 'name':'Tata Motors/TATAMOTORS', 'current_price':'Rs.601.76', 'predicted_price':'Rs.612.79', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'Rs.15.9', 'predicted_current':'1.80%'}
    return JsonResponse(data)

def accenture_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/accenture.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'92.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Accenture/ACN', 'current_price':'$413.9', 'predicted_price':'$442.79', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$46.75', 'predicted_current':'6.52%'}
    return JsonResponse(data)

def adobe_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/adobe.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'91.33%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Adobe/ADBE', 'current_price':'$555.88', 'predicted_price':'$515.21', 'up_down_current':'fas fa-arrow-down text-danger', 'up_down_predicted':'fas fa-arrow-down text-danger', 'up_down_current_since':'$36.87', 'predicted_current':'7.89%'}
    return JsonResponse(data)

def amazon_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/amazon.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Amazon/AMZN', 'current_price':'$3302.11', 'predicted_price':'$3311.36', 'up_down_current':'fas fa-arrow-down text-danger', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$86.34', 'predicted_current':'0.28%'}
    return JsonResponse(data)

def cisco_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/cisco.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'96.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'cisco/CSCO', 'current_price':'$61.64', 'predicted_price':'$66.15', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.68', 'predicted_current':'6.82%'}
    return JsonResponse(data)

def colgate_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/colgate.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'93.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Colgate/CL', 'current_price':'$79.36', 'predicted_price':'$81.04', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$7.44', 'predicted_current':'2.07%'}
    return JsonResponse(data)

def fortis_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/fortis.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'95.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Fortis/FTS', 'current_price':'$45.96', 'predicted_price':'$49.8', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$4.63', 'predicted_current':'7.71%'}
    return JsonResponse(data)

def heromotoco_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/heromotoco.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'93.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'Rs.', 'name':'hero moto/HEROMOTOCO', 'current_price':'Rs.2368.85', 'predicted_price':'Rs.2220.61', 'up_down_current':'fas fa-arrow-down text-danger', 'up_down_predicted':'fas fa-arrow-down text-danger', 'up_down_current_since':'Rs.69.95', 'predicted_current':'6.68%'}
    return JsonResponse(data)

def ibm_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/ibm.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94.86%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'IBM/IBM', 'current_price':'$123.32', 'predicted_price':'$133.3', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$14.2', 'predicted_current':'7.49%'}
    return JsonResponse(data)

def johnson_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/johnson.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'92.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Johnson & johnson/JNJ', 'current_price':'$165.08', 'predicted_price':'$167.46', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$13.01', 'predicted_current':'1.42%'}
    return JsonResponse(data)

def JPMorgan_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/JPMorgan.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'93.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'JP morgan/JPM', 'current_price':'$167.3', 'predicted_price':'$173.11', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$0.86', 'predicted_current':'3.36%'}
    return JsonResponse(data)

def maruti_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/maruti.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'Rs.', 'name':'Maruti/MARUTI', 'current_price':'Rs.8041.64', 'predicted_price':'Rs.8160.37', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'Rs.383.21', 'predicted_current':'1.45%'}
    return JsonResponse(data)

def netflix_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/netflix.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'92.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Netflix/NFLX', 'current_price':'$661.52', 'predicted_price':'$658.39', 'up_down_current':'fas fa-arrow-down text-danger', 'up_down_predicted':'fas fa-arrow-down text-danger', 'up_down_current_since':'$27.67', 'predicted_current':'0.48%'}
    return JsonResponse(data)

def NVIDIA_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/NVIDIA.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'93.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Nvidia/NVDA', 'current_price':'$316.39', 'predicted_price':'$342.41', 'up_down_current':'fas fa-arrow-down text-danger', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$32.72', 'predicted_current':'7.60%'}
    return JsonResponse(data)

def pepsi_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/pepsi.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Pepsi/PEP', 'current_price':'$172.28', 'predicted_price':'$177.9', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$11.97', 'predicted_current':'3.16%'}
    return JsonResponse(data)

def tvsmotors_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/tvsmotors.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'93.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'Rs.', 'name':'TVS Motor/TVSMOTOS', 'current_price':'Rs.702.57', 'predicted_price':'Rs.678.85', 'up_down_current':'fas fa-arrow-down text-danger', 'up_down_predicted':'fas fa-arrow-down text-danger', 'up_down_current_since':'Rs.68.91', 'predicted_current':'3.49%'}
    return JsonResponse(data)

def wallmart_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/wallmart.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'96.65%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Walmart/WMT', 'current_price':'$139.8', 'predicted_price':'$136', 'up_down_current':'fas fa-arrow-down text-danger', 'up_down_predicted':'fas fa-arrow-down text-danger', 'up_down_current_since':'$0.26', 'predicted_current':'2.79%'}
    return JsonResponse(data)
