/* 103-max_state.sql
   displays the max temperature of each state (ordered by State name). */
SELECT state, MAX(value) AS max_temp FROM temperature
       ORDER BY state;
