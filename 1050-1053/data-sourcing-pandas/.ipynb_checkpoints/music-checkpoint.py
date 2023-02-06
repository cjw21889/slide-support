import requests


def get_lyrics(artist, title):
    url = 'https://lyrics.lewagon.ai/search'
    params = {'artist': artist,
              'title': title
             }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['lyrics']
    else:
        return ''