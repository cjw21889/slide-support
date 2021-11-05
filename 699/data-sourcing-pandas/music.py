import requests

def fetch_lyrics(artist, title):
    url = 'https://lyrics.lewagon.ai/search'
    my_params = {'artist': artist, 'title': title}
    response = requests.get(url, params = my_params)
    if response.ok:
        return response.json()['lyrics']
    return ''