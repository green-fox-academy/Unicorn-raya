from flask import Flask, request, render_template, jsonify, make_response, json
from views import emoji,message,mention,thank

app = Flask(__name__)

@app.route("/emoji")
def list_emoji():
    return render_template("emoji.html", emoji = emoji)

@app.route("/message")
def list_message():
    return render_template("message.html", message = message)

@app.route("/mention")
def list_mention():
    return render_template("mention.html", mention = mention)

@app.route("/thank")
def list_thank():
    return render_template("thank.html", thank = thank)

@app.route("/")
def Navigation():
    navi = ["emoji","message","mention","thank"]
    return render_template("Slack_analysis.html",menu = navi)

if __name__ == "__main__":
    app.run()

