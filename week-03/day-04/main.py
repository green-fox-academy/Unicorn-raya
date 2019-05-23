from flask import Flask, request, render_template, jsonify, make_response, json
from movie import movies,movies_id
app = Flask(__name__)
#task 1
# @app.route("/api",methods = ["GET"])
# def api_root():
#     #response = jsonify(a = 12, b = 13)
#     return jsonify(movies)

#task 2
# @app.route("/api/movies/<movie_id>", methods = ["GET"])
# def api_movie_id(movie_id):
#     #response = jsonify(apple = 34, key = request.headers["x-api-key"])
#     return jsonify(movies[int(movie_id)-1])

@app.route("/api/movies/<movie_id>",methods = ["POST"])
def api_movie_post_by_key(movie_id):
    headers = request.headers
    key = headers.get("API_KEY")

    header = "IAMPASSWORD"
    response = ""
    if key == header:
        response = jsonify(movies[int(movie_id)-1])
        response.status_code = 200
    else:
        response = jsonify(error = "Invalid API_KEY")
        response.status_code = 403
    return response

# @app.route("/api", methods = ["POST"])
# def api_root_post():
#     api_key = "Hello" #passport
#     key = request.headers("api_key")
#     response = jsonify(apple = 34, key = request.headers["api_key"])
#     return response

@app.route("/api/movies/<int:movie_id>",methods = ["PUT"])
def api_movie_put(movie_id):
    headers = request.headers
    key = headers.get("API_KEY")
    header = "IAMPASSWORD"
    response = ""
    if key == header:
        if movie_id in movies_id:
            movies[movie_id - 1]["id"] = "the next available integer"
            movies[movie_id - 1]["title"] = "movie title"
            movies[movie_id - 1]["year"] = "year of release"
            movies[movie_id - 1]["genre"] = "genre of the movie"
            movies[movie_id - 1]["discription"] = "a short description"
            response =  jsonify(movies[movie_id - 1]) 
        else:
            response = jsonify(error = '"error": "No movie found with {movie_id} ID"')
            response.status_code = 404
        #response = jsonify(movies[int(movie_id)-1])
    else:
        response = jsonify(error = "Invalid API_KEY")
        response.status_code = 403
    return response


@app.route("/api/movies/<int:movie_id>",methods = ["DELETE"])
def api_movie_delete(movie_id):
    headers = request.headers
    key = headers.get("API_KEY")
    header = "IAMPASSWORD"
    response = ""
    if key == header:
        if movie_id in movies_id:
            movies.pop(movie_id - 1)
            #response =  jsonify(movies[movie_id - 1]) 
        else:
            response = jsonify(error = '"error": "No movie found with {movie_id} ID"')
            response.status_code = 404
        #response = jsonify(movies[int(movie_id)-1])
    else:
        response = jsonify(error = "Invalid API_KEY")
        response.status_code = 403
    return response

@app.route("/api", methods = ["POST"])
def api_root_post():
    response = jsonify(apple = 34, key = request.headers["API_KEY"])
    return response

@app.route("/")
def hello_world():
    return f"hello world"

@app.route("/movie/<username>")
def hello_name(username):
    return render_template("index.html", name = username)

@app.route("/cat")
def cat():
    return f"How are you {request.args.get('name', 'anonymus')}?"

if __name__ == "__main__":
    app.run()

