drink =[
    "cola",
    "water"
]

try:
    index = int(input("?????"))

except IndexError:
    print("xxxxxx")

except ValueError:
    print("pppppppp")

finally:
    print("this will always run")


print("aaaaaaaa")


def add(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    raise TypeError


try:
    print(add("a","b"))
except TypeError:
    print("saadsas")

class MyError(Exception):
    def __init___(self):
        super().__init__()
    
raise MyError