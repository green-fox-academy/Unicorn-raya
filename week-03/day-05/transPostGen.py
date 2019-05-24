authors = [
    {
        "id": 100,
        "name": "John",
        "likes": [
            202,
            200
        ]
    },
    {
        "id": 101,
        "name": "jane",
        "likes" : [
            200
        ]
    }
]
posts = [
    {
        "id": 200,
        "author": 100,
        "content": "Difficulty on insensible reasonable in. From as went he they."
    },
    {
        "id": 201,
        "author": 100,
        "content": "Preference themselves me as thoroughly partiality considered on in estimating."
    },
    {
        "id": 202,
        "author": 101,
        "content": "In as name to here them deny wise this. As rapid woody my he me which."
    }
]

class Data:
    def __init__(self,postID,author_name,context,liked):
        self.postID = postID
        self.author_name = author_name
        self.context = context
        self.liked = liked
    
    def printData(self):
        print(f'PostID: {self.postID}')
        print(f'author_name: {self.author_name}')
        print(f'context: {self.context}')
        print(f'liked: {self.liked}')

manydata = []

def findNameInAuthorsByID(a_id,authors):
    for author in authors:
        if author["id"] == a_id:
            return author["name"] # it is a list
    return ""

def findlikesInAuthorsByID(a_id,authors):
    for author in authors:
        if author["id"] == a_id:
            return author["likes"]
    return ""
    
for post in posts:
    p_id = post["id"]
    a_name = findNameInAuthorsByID(post["author"],authors)
    p_context = post["content"]
    be_liked = []
    for author in authors:
        if post["id"] in author["likes"]:
            be_liked.append(author["name"])
    manydata.append(Data(p_id,a_name,p_context,be_liked))


# for i in manydata:
#     i.printData()
#     print("------------------------------------------------")


    
    


