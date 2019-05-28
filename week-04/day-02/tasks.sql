-- Create a view where you display the reviewer's name and the amount of their review
create view reviewers (reviewer_name,review_amount) as (
    select Reviewer.name,count(*) from Reviewer join rating on Reviewer.rID  = Rating.rID
    group by Rating.rID,Reviewer.name
);

select * from reviewers;

  reviewer_name   | review_amount
------------------+---------------
 Brittany Harris  |             3
 James Cameron    |             1
 Sarah Martinez   |             2
 Elizabeth Thomas |             2
 Chris Jackson    |             3
 Ashley White     |             1
 Mike Anderson    |             1
 Daniel Lewis     |             1
(8 rows)


drop view reviewers;
-- Create a view where you display the movies which have no review
create view not_review (movie) as (
    select title from Movie where mID not in(
        select mID from Rating
    )
);

select * from not_review;

   movie
-----------
 Star Wars
 Titanic
(2 rows)


drop view not_review;
-- Create a view where you display all the directors (do not include null values)
create view directors (director) as (
    select distinct(director) from Movie where director is not null 
);

select * from directors;

     director
------------------
 James Cameron
 Steven Spielberg
 Robert Wise
 George Lucas
 Victor Fleming
(5 rows)

drop view directors;

-- Create a view where you display the movie title and the average rating
create view avg_rating (title,average_rating) as (
    select title,avg(stars) from movie join rating on movie.mID = rating.mID
    group by movie.mID,title
);


select * from avg_rating;

          title          |   average_rating
-------------------------+--------------------
 Raiders of the Lost Ark | 3.3333333333333333
 The Sound of Music      | 2.5000000000000000
 Gone with the Wind      | 3.0000000000000000
 Avatar                  | 4.0000000000000000
 Snow White              | 4.5000000000000000
 E.T.                    | 2.5000000000000000
(6 rows)



drop view avg_rating;