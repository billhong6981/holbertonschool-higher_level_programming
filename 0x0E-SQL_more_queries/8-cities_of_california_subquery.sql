--  lists all the cities of California from database
SELECT id, name FROM cities
       WHERE state_id=
         (SELECT id FROM states
           WHERE name='California')
       ORDER BY id ASC;
