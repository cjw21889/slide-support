import requests

# openlibrary.org is our domain
# /api/books is our endpoint
url = 'https://openlibrary.org/api/books'

# we create a params dict to hold all url param values XYZ.com/xyz?x=*&y=*...
isbn = '0-7475-3269-9'
key = f'ISBN:{isbn}'
params_dict = {
        'bibkeys': key,
        'format': 'json',
        'jscmd': 'data'
        }

# we let the requests library build the full url for us
response = requests.get(url, params=params_dict)
# we can print out the final URL to check the results in the browser
print(response.url)
# We can check if the response was successful 200 / 300 👍 400 - fix your code 👎 500 - servers are down, time to wait 🤞
print(response.status_code)
# Use the .json() method to convert the original json response into a python type
# *** CHECK IN THE BROWSER *** IT COULD BE A LIST OR DICT OR LIST OF DICTS OR NESTED DICTS
print(response.json())
# use correct indexing method to get your data # for lists keys for dicts
print(response.json()[key]['title'])
