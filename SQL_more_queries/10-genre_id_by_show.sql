-- A script used to lists all cities contained in the database.
-- The database name will be passed as an argument of the mysql command

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
JOIN tv_show_genres ON tv_show.id=tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
