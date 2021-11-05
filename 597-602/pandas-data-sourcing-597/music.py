import requests

def fetch_lyrics(artists, title):
    """
    Get lyrics from Seeds Lyrics API. Returns empty string if song not found
    """
    url = f"https://api.lyrics.ovh/v1/{artists}/{title}"
    response = requests.get(url)
    if response.status_code != 200:
        return ''
    data = response.json()
    return data['lyrics']


if __name__ == '__main__':
    print(fetch_lyrics('Beatles', 'Tomorrow'))