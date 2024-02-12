def imdbAvg():
    for i in movies:
        avg = sum(j["imdb"] for j in movies)/len(movies)
    print(avg)

avg = 0
imdbAvg()