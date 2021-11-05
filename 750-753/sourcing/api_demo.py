import requests

isbn = '0-7475-3269-9'
key = f'ISBN:{isbn}'
url = 'https://openlibrary.org/api/books'
param_dict = {'bibkeys': key, 'jscmd': 'data', 'format': 'json'}

response = requests.get(url, params=param_dict)
# print(response.content)
print(response.json()[key]['authors'][0]['name'])
