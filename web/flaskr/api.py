import os
import requests
API_URL = os.environ['API_URL']

def get_api_data(child_url):
    url = API_URL + child_url
    response = requests.get(url)
    return response.json()