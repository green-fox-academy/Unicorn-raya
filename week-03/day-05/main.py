# -*- coding: UTF-8 -*-

from flask import Flask, request, render_template, jsonify, make_response, json
import random
from transPostGen import manydata
app = Flask(__name__)

#============================== Random language 1 ====================================
hello_list = ["hello John","你好，我是警察","*……&&……（&*！@"]
@app.route("/user")
def random_language():
    return render_template("user.html", greeting = hello_list[random.randint(0,2)])

#============================== Random language 2 ====================================
hello_list2 = ["你好","\(@^0^@)/","hello","&^&%*"]
name_list2 = ["ray","🐱","chicken leg","看不懂的中文"]
@app.route("/userH")
def random_language_2():
    return render_template("user2.html", hello = hello_list2[random.randint(0,3)] , someone = name_list2[random.randint(0,3)])

#============================== Products ====================================
articles = [
    {
        "content": "Ne istas culpa ha im negat de. Ii perductae evertenda at desuescam. Nudi per ita sui dare ideo sola omne ordo. Sui sex item sane quum. Paucos sicuti tot qui tantae aliquo strata iis tantas. Mo purgantur at affirmans im reddendum co. Pleraque videntur ut ideamque imaginem ha.",
        "seen": ["John", "Jane", "Bob"]
    },
    {
        "content": "Aliud curam seu venti nihil sed istud volui eae qua. Autho ha falsi fidam tangi ut an tactu. Revera per eandem vox coelum videbo nam virtus. Item olim ei se duas ut. Ut mo ut peccato student adorare et diversa. Praecipuis ad conjunctam me percipitur agnoscerem at perfectius respondere. Horum meo porro uno debeo. Fallacem sentiens ha expertus delapsus dubitare ii. Ex ii efficiente et to perspicuae voluptatem arbitrabar.",
        "seen": ["John", "Jane"]
    },
    {
        "content": "Credendi at nequidem exhibere de. Debeo me dicam ex at ferri digna. Coloribus differant disputari vix cogitandi jam stabilire. Perfacile ut reliquiae perfectae ut. Fuisse falsas captum cui volent notior verbis sui. Meam idem nam ope prae isti quia jure hac. Lor durent has secius fronte usu auditu sumpti. Falso nomen aliud vim calor jam alias annos ubi. Movendi sum creatus vim fas majorem attendo propter. Sui videamus uno profecto refutent rom notitiam innumera potuerit.",
        "seen": ["John"]
    },
    {
        "content": "Potui habeo visus ens mea. An vi re continetur me familiarem negationem. Rei inveniri jam viderunt subducam tam imponere jam. Sub cui more ipsi meum.",
        "seen": []
    }
]
@app.route("/articles")
def list_articles():
    return render_template("articles.html", articles=articles)
#============================== Post ====================================
@app.route("/posts")
def list_posts():
    transformed_posts = manydata
    return render_template("posts.html", posts=transformed_posts)
#==================================== Navigation ==========================
@app.route("/")
def Navigation():
    navi = ["user","userH","articles","posts"]
    return render_template("navi.html",menu = navi)

if __name__ == "__main__":
    app.run()

