
movies = [
    {
    "id": "1",
    "title": "movie title 1",
    "year": "year of release 1",
    "genre": "genre of the movie 1",
    "description": "a short description 1"
    },
    
    {
    "id": "2",
    "title": "movie title 2",
    "year": "year of release 2",
    "genre": "genre of the movie 2",
    "description": "a short description 2"
    },

    {
    "id": "3",
    "title": "movie title 3",
    "year": "year of release 3",
    "genre": "genre of the movie 3",
    "description": "a short description 3"
    }, 
    
    {   
    "id": "4",
    "title": "movie title 4",
    "year": "year of release 4",
    "genre": "genre of the movie 4",
    "description": "a short description 4"
    }
]

movies_id =[]
for movie in movies:
    movies_id.append(int(movie["id"]))

#print(movies_id)