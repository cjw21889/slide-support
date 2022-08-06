import requests

ISBN = 9780747532699
key = f'ISBN:{ISBN}'

url = 'https://openlibrary.org/api/books'
params_dict = {'bibkeys': key,
               'format': 'json',
               'jscmd': 'data'}

response = requests.get(url, params=params_dict).json()
print(response[key]['title'])
