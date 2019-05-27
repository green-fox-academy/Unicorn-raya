-- List the users who registered in 2018 with a .com email address and living in China
select username from users where extract(year from date_of_registration ) = 2018 and  email like '%.com' and country = 'China';

--   username
-- -------------
--  dcrampsy1
--  bsurgenork
--  cdrissell19
--  eturnbull23
--  mlampen2a
-- (5 rows)

-- How many users are there?
select count(id) as user_number from users;

--  user_number
-- -------------
--          100
-- (1 row)

-- How many users registered in 2019?
select count(id) from users where extract(year from date_of_registration ) = 2019; 

--  count
-- -------
--     42
-- (1 row)

-- How many users registered in January?
select count(id) from users where extract(month from date_of_registration) = 01;
--  count
-- -------
--      4
-- (1 row)

-- Which country has the most users?
select country,count(username) from users group by country order by count(username) desc limit 1;

--  country | count
-- ---------+-------
--  China   |    17
-- (1 row)

-- What is the gender ratio?

select (select count(id) from users where gender = 'Female')::DECIMAL/(select count(id) from users where gender = 'Male') as ratio;
select (select count(id) from users where gender = 'Female')*1.0/(select count(id) from users where gender = 'Male') as ratio;

--        ratio
-- --------------------
--  1.3750000000000000
-- (1 row)


-- How many users left at least one field blank?
select count(id) from users where email is null or date_of_registration is null or first_name is null or last_name is null or country is null or gender is null;

--  count
-- -------
--     11
-- (1 row)

-- Which are the 3 most expensive products?
select name,price from products order by price desc limit 3;

--       name      |  price
-- ----------------+----------
--  vestibulum ac  | 149.4001
--  ipsum praesent | 148.3893
--  vestibulum     | 147.0537
-- (3 rows)


-- Which are the 4th and 5th cheapest products?
select name,price from products order by price desc limit 2 offset 3;

--        name       |  price
-- ------------------+----------
--  a suscipit nulla | 146.4756
--  amet nunc        | 145.3140
-- (2 rows)


-- What is the average price for an electric product?

select avg(price) from products;

--          avg
-- ---------------------
--  79.3267320000000000
-- (1 row)


-- How much would it cost me to buy all the toys?

select sum(price) from products;

--     sum
-- -----------
--  7932.6732
-- (1 row)

-- What is the average rating?
select avg(rating) from reviews;

--         avg
-- --------------------
--  3.0933333333333333
-- (1 row)


-- Which product has the best average rating?

select avg(reviews.rating),reviews.product_id,products.name
from reviews left outer join product on reviews.product_id = products.id
group by reviews.product_id, products.name
order by AVG(reviews.rating) limit 1;

-- Which product has the worst rating?
select min(reviews.rating),reviews.product_id,products.name
from reviews left outer join product on reviews.product_id = products.id
group by reviews.product_id, products.name
order by min(reviews.rating) asc limit 1;

-- Which products have no review?
select name from products left outer join reviews on products.id = reviews.product_id where comment is null;
         name
------------------------
 in
 vestibulum ac
 ut nunc vestibulum
 sit amet consectetuer
 lorem
 aliquet massa
 vestibulum ante ipsum
 pede posuere
 fusce consequat nulla
 vestibulum
 a suscipit nulla
 erat eros
 porttitor pede justo
 aliquam augue
 in congue
 nunc purus phasellus
 congue
 odio
 nulla pede ullamcorper
 erat curabitur
 venenatis turpis
 volutpat sapien arcu
 pede posuere
 sit amet diam
 in est
 donec
 vestibulum ac
 duis bibendum
 varius integer
 sed justo pellentesque
 vestibulum ante ipsum
 nunc purus phasellus
 at turpis
 erat curabitur
 sit amet consectetuer
 metus sapien ut
 a pede
 phasellus id
 integer a nibh
 leo maecenas
 a suscipit nulla
 felis fusce
 amet
 vestibulum
 lobortis est
 primis in
 dictumst maecenas ut
 orci
 sit amet sem
 nulla pede ullamcorper
 nunc purus phasellus
 sit amet diam
 pharetra magna
 vestibulum ante ipsum
 primis in
 phasellus id
 pharetra magna
 dictumst maecenas ut
 quis turpis
 primis in
 aliquam augue
 volutpat sapien arcu
 duis bibendum
 fusce consequat nulla
 vel pede
 at turpis
 vel pede
 proin
 in hac
 proin
 quis odio
 at turpis
 lorem
 congue vivamus metus
 etiam
 ipsum primis
 justo
 nulla eget
 mi
 nulla pede ullamcorper
 in hac
 nulla dapibus
 quisque erat eros
 porttitor pede justo
 est
 phasellus
 quam pharetra
 odio
 proin eu
 sit amet consectetuer
 sapien urna pretium
 semper interdum
 proin eu
 erat curabitur
 vel pede
 ut
 in congue
 quis odio
 pede lobortis ligula
 volutpat sapien arcu
 et magnis dis
 primis in
 ut
 amet nunc
 in
 amet nunc
 curae nulla
 sapien
 ipsum praesent
 blandit mi in
 integer aliquet massa
 neque libero convallis
(112 rows)

-- How many reviews are 3 or below without comment?
select count(*) from reviews 
where rating <4 and comment is null;

-- Which user reviewed the most?
select name, count(user_id) as u_count 
from users right outer join reviews on users.id = reviews.user_id 
group by reviews.user_id,users.username
order by count(user_id) desc limit 1;

-- List the average rating for each product
select products.name,avg(reviews.rating),reviews.product_id 
from reviews left outer join products on reviews.product_id = products.id
group by reviews.product_id, products.name
order by product_id;

-- How many days passed since the last review?
select  GETDATE() - max(date) from reviews as DaysGone
