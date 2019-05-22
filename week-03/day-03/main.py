from flask import Flask,request,render_template
import csv
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



def search_by_keyWord(keyword):
    products = {}
    filename = open("Unicorn-raya\week-03\day-03\products.csv")
    tmp_list = []
    products_name =[]
    prick

    for line in filename:
        tmp_list.append(line)
    filename.close()
    for index in range(1,len(tmp_list)):
        tmp_string = list(tmp_list[index].split(";"))
        products[tmp_string[1]] = f"price: {tmp_string[2]}, qty: {tmp_string[3]}" 
    if keyword in products.keys():
        return products[keyword]
    else:
        return "NOPE"


@app.route('/')
def main_page():
    return render_template("search_page.html")

@app.route('/result')
def index_page(movie_index):
    return render_template("search_result_page.html")#,mov = movie[int(movie_index)-1])
    # return f'{request.args.get("test1", "test2")}'
    #http://localhost:5000/movie?test1=hello



if __name__ == '__main__':
    app.debug = False
    app.run(host='localhost', port=5000)