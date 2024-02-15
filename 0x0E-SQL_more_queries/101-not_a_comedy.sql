-- This script list all shows without genre 'Comedy' in 'hbtn_0d_tvshows'

-- 'tv_genres' table contains only one record where name = Comedy

-- Each record should display tv_shows.title

-- You can use max of 2 SELECT statements

SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.title NOT IN (
      SELECT tv_shows.title
      FROM tv_shows
      INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
      INNER JOIN tv_genres g ON tv_show_genres.genre_id = tv_genres.id
      WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
