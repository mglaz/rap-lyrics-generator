import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import ast
import os
from urllib.request import Request, urlopen
import re

base = "https://api.genius.com"
client_access_token = "3MP5a-00vdf3hzeKRDAgMG-fBJh37ZgYx_6_4mIW6YmTI4Rge0s-tOjSUbwIhL-t"
url_list = []

def search(artist_name):
    '''Search Genius API via artist name.'''
    search = "/search?q="
    query = base + search + urllib.parse.quote(artist_name)
    request = urllib.request.Request(query)

    request.add_header("Authorization", "Bearer " + client_access_token)
    request.add_header("User-Agent", "")

    response = urllib.request.urlopen(request, timeout=3)
    raw = response.read()
    data = json.loads(raw)['response']['hits']

    # Gets all of the URL's for songs and appends them an array
    for item in data:
        url_list.append('https://genius.com'+item['result']['path'])


def retrieve_lyrics():
    ''' Retrievies lyrics with the use of song URL'''

    # Counter used to number the songs
    i = 0
    for url in url_list:
        req = Request(url, headers = { 'User-Agent' : 'Mozilla/5.0' })
        webpage = urlopen(req).read()

    # Creating a BeautifulSoup object of the html page for easy extraction of data.
        soup = BeautifulSoup(webpage, 'html.parser')
        song_json = {}
        song_json["Lyrics"] = [];
    # Extract the release date of the song
        for span in soup.findAll('span', attrs = {'class': 'metadata_unit-info metadata_unit-info--text_only'}):
            song_json["Release date"] = span.text.strip()
        for h1 in soup.findAll('h1', attrs = {'class': 'header_with_cover_art-primary_info-title'}):
            song_json["Title"] = h1.text.strip()
        for a in soup.findAll('a', attrs = {'class': 'header_with_cover_art-primary_info-primary_artist'}):
            song_json["Artist"] = a.text.strip()

    #Extract the Lyrics of the song
        for div in soup.findAll('div', attrs = {'class': 'lyrics'}):
            text = div.text.strip().strip()
            # If you want headers like e.g. [Chorus] withing your database, delete this line
            lyrics = re.sub('(\[.*?\])*','', text)
            song_json["Lyrics"].append(lyrics)

    #Extract Title of the song, used later to name the file with lyrics instead of a number
        '''for title in soup.findAll('title'):
            song_name = title.text.replace(' Lyrics | Genius Lyrics','')
            print(song_name)'''
        i += 1
        song_name = str(i)
        print(song_name)
        try:# Writing JSON data
            with open(song_name + '.json' ,'w', encoding = 'ascii') as outfile:
                json.dump(song_json, outfile,  indent = 4, ensure_ascii = True)
        except:
            continue

# Open json with artists names and uses them to search for lyrics
with open("artists_names.json", 'r') as f:
    artist_names = json.load(f)
for num in artist_names:
    search(artist_names[num])
retrieve_lyrics()
