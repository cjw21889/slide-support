import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

raw_movies = soup.find_all('div', class_='lister-item-content')
all_movies = []
for movie in raw_movies:
    title = movie.find('h3', class_='lister-item-header').find('a').text
    duration = movie.find('span', class_='runtime').text
    all_movies.append({'title':title, 'duration':duration})

print(all_movies[0:2])
print(len(all_movies))
