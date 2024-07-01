import requests
import os

# Define the base URL of your Django API
#base_url = 'http://0.0.0.0:8000/api/'
base_url = 'http://0.0.0.0:8000/'

# Make a GET request to fetch JSON data
#print(os.environ["DJANGOACCESS"])
#headers = {'Authorization': 'Token ' + str(os.environ['DJANGOACCESS'])}
headers = {'Authorization': 'Token ' + "b38c2d04f1eeabb743e5ecbe671897cae1794974"}

#test GET request with no token
#response = requests.get(base_url + 'collection_objects/')
#response = requests.get(base_url + 'collection_objects/', headers=headers)
response = requests.get(base_url + 'collection_images/', headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    json_data = response.json()

    # Process the JSON data as needed
    print(json_data)
else:
    print('Failed to fetch data:', response.status_code)
