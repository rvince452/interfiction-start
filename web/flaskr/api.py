import os
import requests
from flask import session, g

API_URL = os.environ['API_URL']

def get_current_user_or_throw()->str:
    retvalue =  get_current_user()
    if not retvalue:
        raise("User not logged in")
    return retvalue
def get_current_user()->str:
    retvalue =  g.user['username'] if g.user else None
    return retvalue

def get_default_headers():
    retvalue = {}
    retvalue['Content-Type'] = 'application/json'
    user = get_current_user()
    if user:
        retvalue['usertoken'] = user
    return retvalue

def get_api_data(child_url):
    url = API_URL + child_url
    response = requests.get(url, headers=get_default_headers())
    # check if the request was successful
    response.raise_for_status()
    return response.json()

def post_api_data(child_url, data):
    url = API_URL + child_url
    response = requests.post(url, json=data, headers=get_default_headers())
    response.raise_for_status()
    return response.json()

def put_api_data(child_url, data):
    url = API_URL + child_url
    response = requests.put(url, json=data, headers=get_default_headers())
    response.raise_for_status()
    return response.json()

def delete_api_data(child_url, data):
    url = API_URL + child_url
    response = requests.delete(url, json=data, headers=get_default_headers())
    response.raise_for_status()
    return response.json()