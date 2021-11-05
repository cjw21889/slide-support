import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/list/ls055386972/'

response = requests.get(url)
soup = BeautifulSoup(response.content,'html.parser')

movies = []
movies_html = soup.find_all('div', class_='lister-item mode-detail')

for movie in movies_html:
    title = movie.find('a').string
    duration = movie.find('span', class_='runtime').string
    movies.append({'Title': title, 'Duration': duration})

print(movies[0])
print(len(movies))
