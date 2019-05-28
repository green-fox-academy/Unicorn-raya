Q1
1.0/1.0分（分级）
Find the titles of all movies directed by Steven Spielberg. 

Note: Your queries are executed using SQLite, so you must conform to the SQL constructs supported by SQLite. 
代码编辑器
1

select title from Movie where director = 'Steven Spielberg';

Correct

Your Query Result:
E.T.
Raiders of the Lost Ark

Expected Query Result:
E.T.
Raiders of the Lost Ark
提交 

Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

重置重置您的答案
Q2
1/1分（分级）
Find all years that have a movie that received a rating of 4 or 5, and sort them in increasing order. 

Note: Your queries are executed using SQLite, so you must conform to the SQL constructs supported by SQLite. 
代码编辑器

select year from Movie where mID in(

    select mID from rating where stars = 4 or stars = 5

)

order by year asc;
按 ESC 键, 或在代码编辑器外单击以退出
正确正确

Correct

Your Query Result:
1937
1939
1981
2009

Expected Query Result:
1937
1939
1981
2009
(Order matters)
提交 Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

正确 (1/1 分) 检查
Q3
1/1分（分级）
Find the titles of all movies that have no ratings. 

Note: Your queries are executed using SQLite, so you must conform to the SQL constructs supported by SQLite. 
代码编辑器

select title from movie where mID not in(

   select mID from rating

);
按 ESC 键, 或在代码编辑器外单击以退出
正确正确

Correct

Your Query Result:
Star Wars
Titanic

Expected Query Result:
Star Wars
Titanic
提交 Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

重置重置您的答案
正确 (1/1 分) 检查
Q4
1/1分（分级）
Some reviewers did not provide a date with their rating. Find the names of all reviewers who have ratings with a NULL value for the date. 

Note: Your queries are executed using SQLite, so you must conform to the SQL constructs supported by SQLite. 
代码编辑器

select name from Reviewer where rID in (

    select rID from rating where ratingDate is null

);
按 ESC 键, 或在代码编辑器外单击以退出
正确正确

Correct

Your Query Result:
Chris Jackson
Daniel Lewis

Expected Query Result:
Chris Jackson
Daniel Lewis
提交 Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

重置重置您的答案
正确 (1/1 分) 检查
Q5
1/1分（分级）
Write a query to return the ratings data in a more readable format: reviewer name, movie title, stars, and ratingDate. Also, sort the data, first by reviewer name, then by movie title, and lastly by number of stars. 

Note: Your queries are executed using SQLite, so you must conform to the SQL constructs supported by SQLite. 
代码编辑器

select Reviewer.name,Movie.title,Rating.stars,Rating.ratingDate

from (Reviewer inner join Rating on Rating.rID = Reviewer.rID) inner join Movie on Movie.mID = Rating.mID

order by Reviewer.name,Movie.title,Rating.stars,Rating.ratingDate
按 ESC 键, 或在代码编辑器外单击以退出
正确正确

Correct

Your Query Result:
Ashley White	E.T.	3	2011-01-02
Brittany Harris	Raiders of the Lost Ark	2	2011-01-30
Brittany Harris	Raiders of the Lost Ark	4	2011-01-12
Brittany Harris	The Sound of Music	2	2011-01-20
Chris Jackson	E.T.	2	2011-01-22
Chris Jackson	Raiders of the Lost Ark	4	<NULL>
Chris Jackson	The Sound of Music	3	2011-01-27
Daniel Lewis	Snow White	4	<NULL>
Elizabeth Thomas	Avatar	3	2011-01-15
Elizabeth Thomas	Snow White	5	2011-01-19
James Cameron	Avatar	5	2011-01-20
Mike Anderson	Gone with the Wind	3	2011-01-09
Sarah Martinez	Gone with the Wind	2	2011-01-22
Sarah Martinez	Gone with the Wind	4	2011-01-27

Expected Query Result:
Ashley White	E.T.	3	2011-01-02
Brittany Harris	Raiders of the Lost Ark	2	2011-01-30
Brittany Harris	Raiders of the Lost Ark	4	2011-01-12
Brittany Harris	The Sound of Music	2	2011-01-20
Chris Jackson	E.T.	2	2011-01-22
Chris Jackson	Raiders of the Lost Ark	4	<NULL>
Chris Jackson	The Sound of Music	3	2011-01-27
Daniel Lewis	Snow White	4	<NULL>
Elizabeth Thomas	Avatar	3	2011-01-15
Elizabeth Thomas	Snow White	5	2011-01-19
James Cameron	Avatar	5	2011-01-20
Mike Anderson	Gone with the Wind	3	2011-01-09
Sarah Martinez	Gone with the Wind	2	2011-01-22
Sarah Martinez	Gone with the Wind	4	2011-01-27
(Order matters)
提交 Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

重置重置您的答案
正确 (1/1 分)