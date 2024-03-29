-- This script uses 'hbtn_0d_tvshows' to list all genres not linked to show 'Dexter'

-- 'tv_shows' table contains only one record where title = Dexter

-- Each record should display tv_genres.name

-- Results must be sorted ascending order by genre name

-- You can use max of two SELECT statements

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
      SELECT tv_genres.name
      FROM tv_genres
      INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
      INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
      WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
