import json

with open('C://Users//Mark//credentials.json', 'r') as f:
    credentials = json.load(f)
    username = credentials['tmdb_username']
    api_key = credentials['tmdb_api_key']