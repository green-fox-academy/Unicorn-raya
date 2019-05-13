# BlogPost
# Create a BlogPost class that has
# an author_name
# a title
# a text
# a publication_date
# Create a few blog post objects:
# "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
# Lorem ipsum dolor sit amet.
# "Wait but why" titled by Tim Urban posted at "2010.10.10."
# A popular long-form, stick-figure-illustrated blog about almost everything.
# "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
# Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention.
#  When I asked to take his picture outside one of IBM’s New York City offices, 
# he told me that he wasn’t really into the whole organizer profile thing.

class BlogPost(object):
    author_name = ""
    title = ""
    text = ""
    publication_date = ""

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
