import requests

isbn = '0-7475-3269-9'
key = f'ISBN:{isbn}'
'https://openlibrary.org/api/books?bibkeys=ISBN:0451526538&format=json&jscmd=data'

response = requests.get(
    'https://openlibrary.org/api/books',
    params={'bibkeys': key, 'format': 'json', 'jscmd': 'data'},
)
import ipdb
ipdb.set_trace()
# .json()

print(response[key]['title'])
