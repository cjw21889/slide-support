import requests

url = 'https://openlibrary.org/api/books'
isbn = '9780747532699'
isbn_key = f'ISBN:{isbn}'
params_dict = {
    'bibkeys': isbn_key,
    'format': 'json',
    'jscmd': 'data'
}

response = requests.get(url, params=params_dict)
response_data = response.json()


print(response_data[isbn_key]['title'])
