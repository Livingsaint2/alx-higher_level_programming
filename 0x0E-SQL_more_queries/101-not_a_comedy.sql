-- lists all shows without the genre Comedy
SELECT shows.title
FROM tv_shows AS shows
WHERE shows.title NOT IN (
  SELECT shows.title
  FROM tv_show_genres AS show_genres
  INNER JOIN tv_genres AS genres ON genres.id = show_genres.genre_id AND genres.name = 'Comedy'
  INNER JOIN tv_shows AS shows ON shows.id = show_genres.show_id
)
ORDER BY shows.title;
