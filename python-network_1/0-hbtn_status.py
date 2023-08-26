#!/usr/bin/python3
import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    content = response.json()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
else:
    print(f"Request failed with status code: {response.status_code}")
