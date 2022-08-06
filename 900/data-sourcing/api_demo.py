import requests

test_url = 'https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data'
base_url = 'https://openlibrary.org/api/books'

ISBN = '9780747532699'
key = f'ISBN:{ISBN}'
params = {'bibkeys':key,
          'format': 'json',
          'jscmd': 'data'}

response = requests.get(base_url, params=params)


print(response.json()[key]['title'])
