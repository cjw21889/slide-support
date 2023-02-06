import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

movies = []

movies_raw = soup.find_all('div', class_='lister-item-content')
x = 0

for movie in movies_raw:
    title = movie.find('h3', class_='lister-item-header').find('a').text
    duration = int(movie.find('span', class_='runtime').text.strip(' min'))
    movies.append({'title': title, 'duration': duration})


print(movies[0])
print(len(movies))
