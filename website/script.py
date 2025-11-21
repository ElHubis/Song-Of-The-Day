from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import random

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)

    
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_track(token):
    letters = 'abcdefghijklmnopqrstuvwxyzåäö'
    random_letter = random.choice(letters)
    offset_int = random.randint(0,1000)
    url = f"https://api.spotify.com/v1/search?q=%{random_letter}%&type=track&limit=1&offset={offset_int}" 
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    return json_result

token = get_token()
searched_track = search_for_track(token)
while searched_track == []:
    searched_track = search_for_track(token)
track_cover = searched_track[0]["album"]["images"][1]["url"]  
track_name = searched_track[0]["name"]

# print(searched_track)
print(track_name)
print(track_cover)