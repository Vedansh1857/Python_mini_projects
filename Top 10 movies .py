import imdb
ia = imdb.IMDb()
search = ia.get_top250_movies()
for i in range(250):
    print(search[i])