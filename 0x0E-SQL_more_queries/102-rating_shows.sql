-- display shows title by rating
SELECT shows.title, SUM(ratings.rate) AS rating
FROM tv_show_ratings AS ratings
INNER JOIN tv_shows AS shows ON ratings.show_id = shows.id
GROUP BY shows.title
ORDER BY rating DESC;
