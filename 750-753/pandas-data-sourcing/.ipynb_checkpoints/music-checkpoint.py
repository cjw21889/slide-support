import requests

def fetch_lyrics_2(artist, title):
    url = 'https://lyrics.lewagon.ai/search?'
    params_dict = {'artist': artist , 'title': title}

    response = requests.get(url, params=params_dict)
    if response.ok:
        return response.json()['lyrics']
    return 'Lyrics Not Found'
