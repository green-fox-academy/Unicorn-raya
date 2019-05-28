Q1
1/1分（评分）
Find the names of all reviewers who rated Gone with the Wind. 
Note: Your queries are executed using SQLite, so you must conform to the SQL constructs supported by SQLite. 
代码编辑器
1
select distinct Reviewer.name from Reviewer left join Rating on Reviewer.rID = Rating.rID
where Rating.mID in (
   select mID from movie where title = "Gone with the Wind"
);
按 ESC 键, 或在代码编辑器外单击以退出
正确正确

Correct

Your Query Result:
Mike Anderson
Sarah Martinez

Expected Query Result:
Mike Anderson
Sarah Martinez
提交 Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.

重置重置您的答案
正确 (1/1 分) 检查
Q2
1/1分（评分）
For any rating where the reviewer is the same as the director of the movie, return the reviewer name, movie title, and number of stars. 

Note: Your queries are executed using SQLite, so you must conform to the SQL constructs supported by SQLite. 
代码编辑器
1
select reviewer.name,movie.title,rating.stars 
from (reviewer inner join Rating on reviewer.rID = Rating.rID) 
inner join Movie on Rating.mID = Movie.mID
where reviewer.name = movie.director;

正确正确

Correct

Your Query Result:
James Cameron	Avatar	5

Expected Query Result:
James Cameron	Avatar	5
