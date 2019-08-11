# Project: 0x0F-python-object_relational_mapping

## Learning Objectives
+ How to connect to a MySQL database from a Python script
+ How to SELECT rows in a MySQL table from a Python script
+ How to INSERT rows in a MySQL table from a Python script
+ What ORM means
+ How to map a Python Class to a MySQL table

## Tasks
+ 0-select_states.py -  lists all states from the database hbtn_0e_0_usa
+ 1-filter_states.py - lists all states with a name starting with N
+ 2-my_filter_states.py - takes in an argument and displays all values in the states table
+ 3-my_safe_filter_states.py -  takes in arguments and displays all values in the states table  
  but safe from MySQL injections!
+ 4-cities_by_state.py - lists all cities from the database hbtn_0e_4_usa
+ 5-filter_cities.py -  takes in the name of a state as an argument and lists all cities of that state,
+ 6-model_state.py - class definition of a State and an instance Base = declarative_base()
+ 7-model_state_fetch_all.py - lists all State objects from the database hbtn_0e_6_usa  via SQLAlchemy
+ 8-model_state_fetch_first.py - prints the first State object from the database hbtn_0e_6_usa
+ 9-model_state_filter_a.py - lists all State objects that contain the letter a
+ 10-model_state_my_get.py - prints the State object with the name passed as argument
+ 11-model_state_insert.py - adds the State object “Louisiana” to the database hbtn_0e_6_usa
+ 12-model_state_update_id_2.py - changes the name of a State object from the database hbtn_0e_6_usa
+ 13-model_state_delete_a.py - deletes all State objects with a name containing the letter a
