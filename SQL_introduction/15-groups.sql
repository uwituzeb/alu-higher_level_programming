-- a script that lists the number of records with the same score in the table second_table
-- result should display score and number of records
-- The list should be sorted by the number of records (descending)
-- The database name will be passed as an argument to the mysql command

from second_table
GROUP BY score
ORDER BY number DESC;
