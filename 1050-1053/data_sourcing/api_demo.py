import requests

url = 'https://openlibrary.org/api/books'
isbn = 9780747532699
key = f"ISBN:{isbn}"

# my_params = {'bibkeys': key,
#         #   'format': 'json',
#           'jscmd': 'data'}

response = requests.get(url)#, params=my_params)
print(response.json()[key])
