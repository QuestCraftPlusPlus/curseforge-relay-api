# Import modules
import os
from sys import int_info
from typing import Optional
from fastapi import FastAPI
from dotenv import load_dotenv
import requests

# Load env variables
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Declare global variables
headers = {
    'Accept': 'application/json',
    'x-api-key': os.environ['API_KEY']
}
url = 'https://api.curseforge.com'

# API listners
@app.get('/')
def read_root():
    return {'Hello': 'Welcome to the Curseforge Relay API!'}

@app.get('/getGame/{gameId}')
def getGameAPI(gameId: int):
    getGame = requests.get(f'{url}/v1/games/{gameId}', headers = headers)
    return getGame.json()

@app.get('/getModloader')
def getModloaderAPI():
    getModloader = requests.get(f'{url}/v1/minecraft/modloader', headers = headers)
    return getModloader.json()

@app.get('/getMod/{modId}')
def getModAPI(modId: int):
    getMod = requests.get(f'{url}/v1/mods/{modId}', headers = headers)
    return getMod.json()

@app.get('/searchMods')
def searchModsAPI(gameId = 432, classId = None, gameVersion = '1.18.2', searchFilter = None, sortField = None, sortOrder = None, modLoaderType = 4, gameVersionTypeId = None, slug = None, index = None, pageSize = None):
    searchMods = requests.get(f'{url}/v1/mods/search', params= {
    'gameId': gameId,
    'classID': classId,
    'gameVersion': gameVersion,
    'searchFilter': searchFilter,
    'sortField': sortField,
    'sortOrder': sortOrder,
    'modLoaderType': modLoaderType,
    'gameVersionTypeId': gameVersionTypeId,
    'slug': slug,
    'index': index,
    'pageSize': pageSize
}, headers = headers)
    return searchMods.json()

@app.get('/getModDescription/{modId}')
def getModDescriptionAPI(modId: int):
    getModDescription = requests.get(f'{url}/v1/mods/{modId}/description', headers = headers)
    return getModDescription.json()

@app.get('/getModFiles/{modId}')
def getModFilesAPI(modId: int):
    getModFiles = requests.get(f'{url}/v1/mods/{modId}/files', headers = headers)
    return getModFiles.json()
