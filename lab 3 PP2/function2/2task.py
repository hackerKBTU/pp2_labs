def highScoreMov():
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            movs.append(movies[i])
    print(movs)

movs = []

highScoreMov()