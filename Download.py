import os
from dotenv import load_dotenv
from DeezerLib import *
from YouTube import *
from pydeezer import Deezer
from pydeezer.constants import track_formats

import json
import requests

load_dotenv()
DEEZER_TOKEN = os.getenv("DEEZER_TOKEN")
RUTA_DES = os.getenv("RUTA_DES")
def Descargar_Cancion(Direccion, id_, token):
    deezer = Deezer(arl=token)
    track = deezer.get_track(id_)
    track["download"](Direccion, quality=track_formats.MP3_320)


def Descargar(url):
    Titulos = getTitle(url)
    if len(Titulos) > 0:
        cont = 0
        for Titulo in Titulos:
            ID = Buscar_From_PYL_Download(Titulo)
            if ID != None:
                Descargar_Cancion(RUTA_DES, ID, DEEZER_TOKEN)
            


init_deezer_session(DEEZER_TOKEN)


