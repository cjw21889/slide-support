import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
movies_list = soup.find_all('div', class_='lister-item-content')
movies = []

for movie in movies_list:
    title = movie.find('h3', class_='lister-item-header').find('a').text
    duration = int(movie.find('span', class_='runtime').text.strip(' min'))
    movies.append({'Title': title, 'Duration': duration})

print(movies[0:2])
print(len(movies))
