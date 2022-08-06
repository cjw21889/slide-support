import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

movies_raw = soup.find_all('div', class_='lister-item-content')
all_movies = []

for movie in movies_raw:
    title  = movie.find('h3', class_='lister-item-header').find('a').string
    duration = movie.find('span', class_='runtime').string

    all_movies.append({'Title': title, 'Duration': duration})

print(all_movies[0:2])
print(len(all_movies))
