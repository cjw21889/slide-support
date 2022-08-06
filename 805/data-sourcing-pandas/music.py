import requests

def fetch_lyrics(artist, title):
    base_url = 'https://lyrics.lewagon.ai/search'
    params_dict = {'artist': artist,
              'title': title}

    response = requests.get(base_url,params=params_dict)
    if response.ok:
        return response.json().get('lyrics', '')
    return ''