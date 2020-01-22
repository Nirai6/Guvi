movie_box = {
    "Robin Hood: Men in Tights": {
        "imdb_stars": 6.7,
        "length": 104,
        "stars": [ {"name": "Cary Elwes", "imdb": "nm0000144", "role": "Robin Hood"},
                   {"name": "Richard Lewis", "imdb": "nm0507659", "role": "Prince John"} ]
    }
}

print("IMBD Star rating",movie_box["Robin Hood: Men in Tights"]["imdb_stars"],"Length of movie",movie_box["Robin Hood: Men in Tights"]["length"],"mins")