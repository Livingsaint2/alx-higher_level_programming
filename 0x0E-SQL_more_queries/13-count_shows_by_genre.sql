-- count number of shows of each genre
SELECT genres.name AS genre, COUNT(show_genres.show_id) AS number_of_shows
FROM tv_show_genres AS show_genres
INNER JOIN tv_genres AS genres
ON show_genres.genre_id = genres.id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
