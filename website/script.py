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
    auth_string = client_id + ":" + client_secret
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
    url = 'https://api.spotify.com/v1/search?q=%' + random_letter + '%&type=track&limit=1'
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"][0]["album"]["name"]
    return json_result

def get_album_name(token):
    url = "https://api.spotify.com/v1/albums/21b4cDNse2AMpj94ykfuON"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["name"]
    return json_result

def get_album_cover(token):
    url = "https://api.spotify.com/v1/albums/21b4cDNse2AMpj94ykfuON"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["images"][1]["url"]
    return json_result

token = get_token()
searched_track = search_for_track(token)
album_name = get_album_name(token)
album_cover = get_album_cover(token)
# print(token)
print(searched_track)
# print(album_name)
# print(album_cover)