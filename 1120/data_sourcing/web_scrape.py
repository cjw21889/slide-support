import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/list/ls055386972/'

# initiate a call response cycle usings requests
response = requests.get(url)
# the response content will not be a json it will be html
# can't just use .json() need to use beautiful soup to get it into python
soup = BeautifulSoup(response.content, 'html.parser')

all_movies = []
# use find all to split your html into workable smaller sections
raw_movies = soup.find_all('div', class_='lister-item-content')
for movie in raw_movies:
    # use your find methods to drill into your smaller sections
    # use .text or .string to get the data pubslished on the actual website
    # .string gets the text directly on that tag
    # .text gets the text on the tag + text on any other nested tags
    title = movie.find('h3', class_='lister-item-header').find('a').text
    runtime = movie.find('span', class_='runtime').text
    all_movies.append({'Title': title, 'Runtime': runtime})

print(all_movies)
