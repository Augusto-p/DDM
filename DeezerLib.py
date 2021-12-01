from typing import Optional, Sequence
import urllib.parse
import html.parser
import requests
TYPE_TRACK = "track"
session = None
def init_deezer_session(token):
    global session
    header = {
        'Pragma': 'no-cache',
        'Origin': 'https://www.deezer.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
        'Cache-Control': 'no-cache',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://www.deezer.com/login',
        'DNT': '1',
    }
    session = requests.session()
    session.headers.update(header)
    session.cookies.update({'arl': token})
def deezer_search(search, search_type):
    if search_type not in [TYPE_TRACK]:
        print("ERROR: search_type is wrong: {}".format(search_type))
        return []
    search = urllib.parse.quote_plus(search)
    resp = session.get("https://api.deezer.com/search/{}?q={}".format(search_type, search)).json()['data']
    return_nice = []
    for item in resp:
        i = {}
        if search_type == TYPE_TRACK:
            i['id'] = str(item['id'])
            i['id_type'] = TYPE_TRACK
            i['title'] = item['title']
            i['img_url'] = item['album']['cover_small']
            i['album'] = item['album']['title']
            i['album_id'] = item['album']['id']
            i['artist'] = item['artist']['name']
            i['preview_url'] = item['preview']
        return_nice.append(i)
    return return_nice
def search_title_artist(title, artist):
    song = deezer_search(title, "track")
    var = ""
    i = 0
    while i != len(song):
        if (song[i]["artist"]).upper() in artist.upper():
            var = song[i]["id"]
            i = len(song)
        elif (song[i]["title"]).upper() in artist.upper() :
            var = song[i]["id"]
            i = len(song)
        else: i = i +1
    return var


def Buscar_From_PYL_Download(Titulo):
    Texto = ""
    for Parte in Titulo:
        Texto = Texto +" "+ Parte
    
    if "track" not in [TYPE_TRACK]:
        print("ERROR: track is wrong: {}".format("track"))
        return []
    search = urllib.parse.quote_plus(Texto)
    resp = session.get("https://api.deezer.com/search/{}?q={}".format("track", search)).json()['data']

    if len(resp) > 0:
        cont = 0
        a = 1
        while a != 0:
            if resp[cont]['id'] != None:
                if  "track" == TYPE_TRACK:
                    a = 0
                else:
                    cont = cont + 1
            else:
                cont = cont + 1
        return str(resp[cont]['id'])
            
    

