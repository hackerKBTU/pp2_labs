def imdbCatAvg():
    for i in range(len(movies)):
        if movies[i]["category"] == cat:
            movs.append(movies[i])
    avg = sum(j["imdb"] for j in movs)/len(movs)
    print(avg)

cat = input()
movs = []
avg = 0
imdbCatAvg()