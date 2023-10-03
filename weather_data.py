import requests
import json

def pressure(userdata_date):
    
    response = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    api_data = response.json()
    
    items = api_data["list"]
    indx = None
    for i in items:
        if i["dt_txt"] == userdata_date:
            indx = items.index(i)
        
    innerlist = items[indx]
    result=innerlist['main']['pressure']
    return result

def temperature(userdata_date):
    
    
    response = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    api_data = response.json()
    
    items = api_data["list"]

    indx = None
    indx = None
    for i in items:
        if i["dt_txt"] == userdata_date:
            indx = items.index(i)
        
    innerlist = items[indx]
    result=innerlist['main']['temp']
    return result

def windspeed(userdata_date):

    
    response = requests.get("https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22")
    api_data = response.json()
    
    items = api_data["list"]

    indx = None
    
    for i in items:
        if i["dt_txt"] == userdata_date:
            indx = items.index(i)
        
    innerlist = items[indx]
    result=innerlist['wind']['speed']
    return result

   