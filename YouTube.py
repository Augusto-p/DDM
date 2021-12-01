import re
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv('GOOGLE_API_KEY')
def ClearName(name):
    end = []
    resultado = name.lower()
    if "bzrp" in resultado:
        text = resultado.split(" || ")[1]
        end.append("bizarap")
        end.append(text)

    else:
        if '(' in resultado:
            parentesis = re.findall('\(([^)]+)', resultado)
            for text in parentesis:
                resultado = resultado.replace(text, '')
            resultado = resultado.replace(' ()', '')
        
        split = resultado.split(' - ')
        for text in split:
            text = text.split(' ft.')[0]
            text = text.split(' feat')[0]
            text = text.split(' | ')[0]
            if "," in text:
                text = text.split(',')[0]
            end.append(text)
    return end

def getTitle(url):
    resultados = []
    ID = url.replace("https://www.youtube.com/playlist?list=", "")
    info = requests.get('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50'+'&key='+API_KEY+'&playlistId='+ID)
    info = info.json()
    for item in info['items']:
        resultados.append(ClearName(item['snippet']['title']))
    return resultados



