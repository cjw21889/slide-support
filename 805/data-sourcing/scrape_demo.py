import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

raw_movies = soup.find_all('div', class_='lister-item')

movies = []
for movie in raw_movies:
    title = movie.find('h3', class_='lister-item-header').find('a').string
    duration = int(movie.find('span', class_='runtime').string.strip(' min'))
    movies.append({'Title': title, 'Duration': duration})

print(len(movies))
print(movies[0])
print(movies[-1])
