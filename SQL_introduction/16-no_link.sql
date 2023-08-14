-- script that lists all records of the table second_table of the database hbtn_0c_0
-- results should display score and name in descending order

SELECT score, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY score DESC;
