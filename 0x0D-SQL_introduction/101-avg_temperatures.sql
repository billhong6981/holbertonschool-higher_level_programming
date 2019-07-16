/* 101-avg_temperatures.sql
   displays the average temperature (Fahrenheit)
   by city ordered by temperature (descending). */
SELECT city, AVG(value) AS avg_temp FROM temperature ORDER BY avg_temp DESC;
