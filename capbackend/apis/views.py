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
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def zara_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/zara.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def facebook_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/fb.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def tata_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/tatamotors.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def accenture_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/accenture.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def adobe_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/adobe.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def amazon_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/amazon.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def cisco_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/cisco.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def colgate_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/colgate.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def fortis_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/fortis.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def heromotoco_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/heromotoco.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def ibm_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/ibm.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def johnson_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/johnson.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def JPMorgan_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/JPMorgan.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def maruti_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/maruti.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def netflix_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/netflix.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def NVIDIA_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/NVIDIA.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def pepsi_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/pepsi.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def tvsmotors_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/tvsmotors.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)

def wallmart_stock_api(request):
    loaded=sarimax.SARIMAXResultsWrapper.load('apis/arimaModels/wallmart.pkl')
    predictions = loaded.predict(start=77,end=(85)+3,typ='levels')
    print(predictions)
    data={'predictions':list(predictions),'accuracy':'94%','labels':['April 2021','May 2021','June 2021','July 2021','August 2021','September 2021','October 2021','November 2021','December 2021','January 2022','Feburary 2022','March 2022'],'cur':'$', 'name':'Apple/APL', 'current_price':'$167.76', 'predicted_price':'$175.47', 'up_down_current':'fas fa-arrow-up text-success', 'up_down_predicted':'fas fa-arrow-up text-success', 'up_down_current_since':'$6.66', 'predicted_current':'4.39%'}
    return JsonResponse(data)
