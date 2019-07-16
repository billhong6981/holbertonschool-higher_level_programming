--  lists all records that match condition in order
SELECT score, name FROM second_table
       HAVING score >= 10 ORDER BY score DESC;
