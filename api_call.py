import requests

def info_call(url):
    #url = f'https://540zfa.deta.dev/items/{id}'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    item_id = response.json()['item_id']
    item_name = response.json()['item_name']
    item_type = response.json()['item_type']
    item_desc = response.json()['item_desc']
    _ = response.json()['quantity']
    price = response.json()['price']
    return item_name, item_type, item_desc, price

def ques_call(url):
    #url = f'https://540zfa.deta.dev/items/{id}/{question}'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    return response
