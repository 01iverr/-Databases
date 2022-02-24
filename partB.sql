SELECT extract(year from release_date) as year, COUNT(*) FROM MOVIES_METADATA GROUP BY year order by year;

SELECT COUNT(id) FROM Movies_metadata where genres like '%" + i + "%';

SELECT extract (year from release_date) as year ,COUNT(id) FROM Movies_metadata where genres like '%" + i + "%' group by year order by year;

SELECT round(cast(avg(rating) as numeric), 2) FROM Ratings join links on ratings.movieid = links.movieid join movies_metadata on movies_metadata.imdb_id = links.imdbid where genres like '%" + i + "%';

SELECT userid , COUNT(rating) FROM Ratings GROUP BY userid order by userid;

SELECT userid , round(cast(avg(rating) as numeric), 2) FROM Ratings GROUP BY userid order by user

create view table_view as SELECT userid , COUNT(rating) as Total_Ratings, round(cast(avg(rating) as numeric), 2) as AVG_Rating FROM Ratings_Small GROUP BY userid order by userid
select * from view_table;