# pip install request
from requests import request
from pprint import pprint

def get_all_object_details():
    url = "https://api.restful-api.dev/objects"
    headers = {}
    payload = {}
    response = request("GET", url, headers=headers, data=payload)
    pprint(response.json())
    pprint(response.status_code)


#get_all_object_details()
# [{'id': '1', 'name': 'Google Pixel 6 Pro', 'data': {'color': 'Cloudy White', 'capacity': '128 GB'}}, {'id': '2', 'name': 'Apple iPhone 12 Mini, 256GB, Blue', 'data': None}, {'id': '3', 'name': 'Apple iPhone 12 Pro Max', 'data': {'color': 'Cloudy White', 'capacity GB': 512}}, {'id': '4', 'name': 'Apple iPhone 11, 64GB', 'data': {'price': 389.99, 'color': 'Purple'}}, {'id': '5', 'name': 'Samsung Galaxy Z Fold2', 'data': {'price': 689.99, 'color': 'Brown'}}, {'id': '6', 'name': 'Apple AirPods', 'data': {'generation': '3rd', 'price': 120}}, {'id': '7', 'name': 'Apple MacBook Pro 16', 'data': {'year': 2019, 'price': 1849.99, 'CPU model': 'Intel Core i9', 'Hard disk size': '1 TB'}}, {'id': '8', 'name': 'Apple Watch Series 8', 'data': {'Strap Colour': 'Elderberry', 'Case Size': '41mm'}}, {'id': '9', 'name': 'Beats Studio3 Wireless', 'data': {'Color': 'Red', 'Description': 'High-performance wireless noise cancelling headphones'}}, {'id': '10', 'name': 'Apple iPad Mini 5th Gen', 'data': {'Capacity': '64 GB', 'Screen size': 7.9}}, {'id': '11', 'name': 'Apple iPad Mini 5th Gen', 'data': {'Capacity': '254 GB', 'Screen size': 7.9}}, {'id': '12', 'name': 'Apple iPad Air', 'data': {'Generation': '4th', 'Price': '419.99', 'Capacity': '64 GB'}}, {'id': '13', 'name': 'Apple iPad Air', 'data': {'Generation': '4th', 'Price': '519.99', 'Capacity': '256 GB'}}]
# 200


def get_specific_objects_details():
    url = "https://api.restful-api.dev/objects?id=3&id=5&id=10"
    headers = {}
    payload = {}
    response = request("GET", url, headers=headers, data=payload)
    pprint(response.json())
    pprint(response.status_code)

#get_specific_objects_details()
"""
[{'data': {'capacity GB': 512, 'color': 'Cloudy White'},
  'id': '3',
  'name': 'Apple iPhone 12 Pro Max'},
 {'data': {'color': 'Brown', 'price': 689.99},
  'id': '5',
  'name': 'Samsung Galaxy Z Fold2'},
 {'data': {'Capacity': '64 GB', 'Screen size': 7.9},
  'id': '10',
  'name': 'Apple iPad Mini 5th Gen'}]
200
"""


def get_one_object_details():
    url = "https://api.restful-api.dev/objects/7"
    headers = {}
    payload = {}
    response = request("GET", url, headers=headers, data=payload)
    pprint(response.json())
    pprint(response.status_code)

get_one_object_details()
"""
{'data': {'CPU model': 'Intel Core i9',
          'Hard disk size': '1 TB',
          'price': 1849.99,
          'year': 2019},
 'id': '7',
 'name': 'Apple MacBook Pro 16'}
200


"""
