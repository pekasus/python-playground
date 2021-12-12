import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

html = requests.get(URL).text

soup = BeautifulSoup(html, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
for n in range(len(movie_titles) - 1, -1, -1):
    print(movie_titles[n])

movies = movie_titles[::-1]

with open("movies.txt", "w") as f:
    for movie in movies:
        f.write(f"{movie}\n")