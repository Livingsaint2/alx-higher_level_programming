-- list all shows, and all genres linked to that show
SELECT shows.title, genres.name
FROM tv_shows AS shows
LEFT JOIN tv_show_genres AS show_genres ON show_genres.show_id = shows.id
LEFT JOIN tv_genres AS genres ON show_genres.genre_id = genres.id
ORDER BY shows.title, genres.name;
