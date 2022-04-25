import json
from fastapi import FastAPI
# Import modules
import os
from dotenv import load_dotenv
from yaml import load
import requests

# Load env variables
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Declare global variables
headers = {
    'Accept': 'application/json',
    'x-api-key': os.getenv('API_KEY')
}
url = 'https://api.curseforge.com'
gameId = '432'

# Create requests
getGame = requests.get(f'{url}/v1/games/{gameId}', headers = headers)
getModloader = requests.get(f'{url}/v1/minecraft/modloader', headers = headers)
getMod = requests.get(f'{url}/v1/mods/308702', headers = headers)
getVersions = requests.get(f'{url}/v1/games/{gameId}/versions', headers = headers)
searchMods = requests.get(f'{url}/v1/mods/search', params= {
    'gameId': gameId,
    'classID': '6',
}, headers = headers)

# Create API listners
@app.get('/getGame')
def getGameAPI():
    return getGame.json()

@app.get('/getModloader')
def getModloaderAPI():
    return getModloader.json()

@app.get('/getMod')
def getModAPI():
    return getMod.json()

@app.get('/getVersions')
def getVersionsAPI():
    return getVersions.json()

@app.get('/searchMods')
def searchModsAPI():
    return searchMods.json()