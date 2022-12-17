import json
import spotipy
import webbrowser
import time
import pyautogui as pag
from selenium import webdriver
import matplotlib.pyplot as plt
import cv2
from deepface import DeepFace

def imgcap_fun(face):
    try :
        obj=DeepFace.analyze(face, actions = ['emotion'])
        return obj
    except :
        return "Face not Detected"

def facecap() :
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    return frame



username = "nvc60v65mqp4z7tfxhz1m58qn"
client_id = "c085fa7255044a9ca408236539c6a46d"
client_secret = "42fdbd884bd54785bcf1ffa4a793fb4f"
redirect_url = "http://google.com/callback/"

oauth_object = spotipy.SpotifyOAuth(client_id, client_secret, redirect_url)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

# To print the response in readable format.
print(json.dumps(user_name, sort_keys=True, indent=4))

search_song = imgcap_fun(facecap())
search_song = search_song["dominant_emotion"] + "songs"
print("Searching for",search_song)
#search_song = input("Enter the query string : ")
results = spotifyObject.search(search_song, 1, 0, "track")

song_link = results["tracks"]["items"][0]["external_urls"]["spotify"]

name = results["tracks"]["items"][0]["name"]
artist = results["tracks"]["items"][0]['album']['artists'][0]['name']
print(f"Playing {name} by {artist}")
time.sleep(1)
driver = webdriver.Firefox()
driver.get(song_link)
#time.sleep(10)
#driver.close()
