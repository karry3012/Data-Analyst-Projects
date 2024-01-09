--Q1: Who is the senior most employee based on job title? - "Mohan Madan"
select first_name ||' '|| last_name
from employee
order by levels DESC
limit 1;

--Q2 :Which countries have the most Invoices? - "USA"-	131
select billing_country , count(*) as total
from invoice 
group by billing_country
order by total DESC;

--03: What are top 3 values of total invoice? - "23.759999999999998,19.8,19.8"
select total
from invoice
order by total desc
limit 3;

--Q4: Which city has the best customers? We would like to throw a promotional Music Festival in the city we made the most money. Write a query that returns one city that has the highest sum of invoice totals.
--Return both the city name & sum of all invoice totals? -"Prague	273.24000000000007"

select billing_city , sum(total) as t
from invoice
group by(billing_city)
order by t desc
limit 1;

-- Q5: Who is the best customer? The customer who has spent the most money will be declared the best customer. 
--Write a query that returns the person who has spent the most money.
-- "R","Madhav","144.54000000000002"

select c.first_name, c.last_name  , sum(i.total) as t
from customer c
join invoice i
on c.customer_id = i.customer_id
group by c.customer_id
order by t desc
limit 1;

--Q6 Q1: Write query to return the email, first name, last name, & Genre of all Rock
--Music listeners. Return your list ordered alphabetically by email starting with A
select * from genre;
select distinct c.first_name, c.last_name  , c.email 
from customer c
join invoice iv on c.customer_id = iv.customer_id
join invoice_line ivl on iv.invoice_id = ivl.invoice_id
where ivl.track_id In(
select t.track_id from track as t
join genre as g 
on t.genre_id = g.genre_id
where g.name = 'Rock')
order by c.email;

--Q7:Return all the track names that have a song length longer than the average 
--song length. Return the Name and Milliseconds for each track. Order
--by the song length with the longest songs listed first.
select name, milliseconds
from track
where milliseconds >(
	select avg(milliseconds)
				from track)
order by milliseconds desc;