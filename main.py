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
    'x-api-key': os.getenv('API_KEY')
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

@app.get('/getVersions')
def getVersionsAPI(gameId: int):
    getVersions = requests.get(f'{url}/v1/games/{gameId}/versions', headers = headers)
    return getVersions.json()

@app.get('/searchMods')
def searchModsAPI(gameId: int, classId: int, categoryId: int, gameVersion: str, searchFilter: str, sortField: int, sortOrder: int, modLoaderType: int, gameVersionTypeId: int, slug: str, index: int, pageSize: int):
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

@app.get('/getModDownloadURL')
def getModDownloadURLAPI(modId: int, fileId: int):
    getModDownloadURL = requests.get(f'{url}/v1/mods/{modId}/files/{fileId}/download-url', headers = headers)
    return getModDownloadURL.json()
