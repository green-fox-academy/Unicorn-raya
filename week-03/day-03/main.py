from flask import Flask,request,render_template
import csv
from functions import splitdata2list,search_by_price,search_by_product_name,search_by_qtys
app = Flask(__name__)
#task 1

# @app.route('/index')
# def main_page():
#     return render_template("index.html")

# @app.route('/<page>')
# def movies_page(page):
#     return render_template(f"{page}")

#task 2 

# def readLocalFile(filename):
#     movie_dic = []
#     with open(filename,'r+') as file:
#         lines = file.readlines()
#         for line in lines:
#             movie_dic.append(list(line.split())[1])            
#     return movie_dic 

# @app.route('/')
# def main_page():
#     return render_template("index.html")

# @app.route('/<movie_index>')
# def index_page(movie_index):
#     # return f'{request.args.get("test1", "test2")}'
#     #http://localhost:5000/movie?test1=hello
#     movie = readLocalFile("Unicorn-raya\week-03\day-03\movie.txt")
#     return render_template("movie.html",mov = movie[int(movie_index)-1])

# task 3
@app.route('/')
def main_page():
    return render_template("search_page.html")

@app.route('/result',methods = ["POST"])
def result_page():
    name = request.form.get('product_name')
    price = request.form.get('price_name')
    qty = request.form.get('qty_name')

    pnameLst,priceLst,qtysLst = splitdata2list()
    price_qtys = search_by_product_name(name,pnameLst,priceLst,qtysLst)
    name_qtys =search_by_price(price,pnameLst,priceLst,qtysLst)
    name_price =search_by_qtys(qty,pnameLst,priceLst,qtysLst)
    #len(price_qtys)  len(name_qtys) len(name_price)
    if name:
        return render_template("search_result_page.html",resultlist = price_qtys)
    if price:
        return render_template("search_result_page.html",resultlist = name_qtys)
    if qty:
        return render_template("search_result_page.html",resultlist = name_price)
    # return f'{request.args.get("test1", "test2")}'
    #http://localhost:5000/movie?test1=hello


if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=5000)