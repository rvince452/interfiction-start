import requests

url = "https://example.com/api/endpoint"  # Replace with your API endpoint URL

headers = {
    "token": "your_token_value",
    "fruit": "your_fruit_value"
}

data = {
    "key1": "value1",
    "key2": "value2"
}

response = requests.post(url, headers=headers, data=data)

print(response.status_code)
print(response.json())
