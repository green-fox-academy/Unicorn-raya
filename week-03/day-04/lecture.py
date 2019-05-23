from flask import Flask, request, render_template, jsonify, make_response, json

app = Flask(__name__)

@app.route("/api")
def api_root():
    response = jsonify(a = 12, b = 13)
    return response

@app.route("/api", methods = ["POST"])
def api_root_post():
    response = jsonify(apple = 34, key = request.headers["x-api-key"])
    return response


@app.route("/")

def hello_world():
    return f"hello world"

@app.route("/<username>")
def hello_name(username):
    return render_template("index.html", name = username)

@app.route("/cat")
def cat():
    return f"How are you {request.args.get('name', 'anonymus')}?"

if __name__ == "__main__":
    app.run()