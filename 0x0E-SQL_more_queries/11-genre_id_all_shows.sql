-- list all shows
-- genre_id displays NULL if not exists
SELECT shows.title, show_genres.genre_id
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres
ON shows.id = show_genres.show_id
ORDER BY shows.title, show_genres.genre_id;
