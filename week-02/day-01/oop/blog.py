# Blog
# Reuse your BlogPost class
# Create a Blog class which can
# store a list of BlogPosts
# add BlogPosts to the list
# delete(int) one item at given index
# update(int, BlogPost) one item at the given index and update it with another BlogPost
from blogpost import BlogPost
class Blog(object):
    def __init__(self):
        self.blog_list = []
        Lorem_lpsum = BlogPost()
        Wait_but_y = BlogPost()
        one_engineer = BlogPost()

        Lorem_lpsum.author_name = "John Doe"
        Lorem_lpsum.title = "Lorem Lpsum"
        Lorem_lpsum.text = "Lorem ipsum dolor sit amet"
        Lorem_lpsum.publication_date = "2000.05.04"


        Wait_but_y.author_name = "Tim Urban"
        Wait_but_y.title = "Wait but why"
        Wait_but_y.text = "A popular long-form, stick-figure-illustrated blog about almost everything."
        Wait_but_y.publication_date = "2010.10.10"

        one_engineer.author_name = "William Turton"
        one_engineer.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
        one_engineer.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."
        one_engineer.publication_date = "2017.03.28."
        
        self.blog_list.append(Lorem_lpsum)
        self.blog_list.append(Wait_but_y)
        self.blog_list.append(one_engineer)
    
    def add_blogPost(self,blogpost):
        self.blog_list.append(blogpost)

    def delete_blogPost(self,index):
        del self.blog_list[index]    

    def update_blogPost(self,index,blogpost):
        if index < len(self.blog_list):
            self.blog_list[index] = blogpost
        else:
            self.blog_list.append(blogpost)



