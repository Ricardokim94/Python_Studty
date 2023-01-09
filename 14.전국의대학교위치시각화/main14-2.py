import requests
import json
import pandas as pd
from tqdm import tqdm
import numpy as np

test_data = pd.DataFrame([{'name':'정왕동,한국산업기술대학교','address':'경기도 시흥시 산기대학로237'}])

url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4325&refine=true&simple=false&format=json&type=road'

# road_type = 'ROAD' #도로명주소
# road_type2 = 'PARCEL' #지번주소
road_type = 'PARCEL'
address = '&address='
keys = '&key='
primary_key = '36064C14-3A6C-320F-927D-90FF76B8F9FC'
geocode = pd.DataFrame(columns = ['name','address', 'x', 'y'])

def request_geo(road):
    page = requests.get(url+params+address+road+keys+primary_key)
    json_data = page.json()
    return json_data

def extraction_geo(test_data):
    geocode = pd.DataFrame(columns = ['name','address', 'x', 'y'])
    none = None
    for idx, road in tqdm(zip(test_data.index ,test_data['address'])):
        name = str(test_data['name'][idx])
        if len(str(road)) <= 5:
            geocode = geocode.append(
                    pd.DataFrame({'name':name,
                    'address':road,
                    'x':none,
                    'y':none},
                    index=[idx]))
            continue

        json_data = request_geo(road)

        if json_data['response']['status'] == 'NOT_FOUND' or json_data['response']['status'] == 'ERROR':
            geocode = geocode.append(
                    pd.DataFrame({'name':name,
                    'address':road,
                    'x':none,
                    'y':none},
                    index=[idx]))
            continue

        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']

        geocode = geocode.append(
            pd.DataFrame({'name':name,
                    'address':road,
                    'x':float(x),
                    'y':float(y)},
                    index=[idx]))
    return geocode

result = extraction_geo(test_data)
# def request_geo(road):
#     page = requests.get(url+params+road_type+address+road+keys+primary_key)
#     json_data = page.json()
#     if json_data['response']['status'] == 'OK':
#         x = json_data['response']['result']['point']['x']
#         y = json_data['response']['result']['point']['y']
#         return x,y
#     else:
#         x=0
#         y=0
#         return x,y
# x,y = request_geo("경기도 시흥시 산기대학로237 (정왕동,한국산업기술대학교)")

# print(f'x값: {x}')
# print(f'y값: {y}')


