# Import modules
import os
from fastapi import FastAPI
from typing import Optional
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
def searchModsAPI(categoryId: Optional[int], gameVersion: Optional[str], searchFilter: Optional[str], sortField: Optional[int], sortOrder: Optional[int], modLoaderType: Optional[int], gameVersionTypeId: Optional[int], slug: Optional[str], index: Optional[int], pageSize: Optional[int], gameId = 432, classId = 6):
    searchMods = requests.get(f'{url}/v1/mods/search', params= {
    'gameId': gameId,
    'classID': classId,
    'categoryId': categoryId,
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