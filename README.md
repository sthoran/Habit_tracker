# Habit Tracker

### Habit tracker is an open source habit manifestation program. Document the habit tracking process and receive automated analysis evaluaions of your successes and difficulties that accompany you on the path to the new you.

 ## <u> Features

* Terminal operated program.
* Data is stored permanently in a local database (SQLite). User has ability to change database entry by adding or deleteing habits.
* User can user three time schedules for habit tracking (daily, weekly, monthly).
* Successfully completed habits can be documented with the "check off" feature. The day of completion is than documented in the database.
* User entries are secured by registration via username and user password
* Analysis of habit tracking process does include:
    1. Streak count for a user-defined habit (Streak means, longest consecutive period of successfully completed habits)
    2. Streak count and struggle count of all habits (Struggle means, longest consecutive period of not checked-off habits)


### <u> Installation
   

#### Download the source code

git clone https://github.com/sthoran/OOP_habit_tracker.git

### <u> Run instructions

* Download the source file in a directory of your choice. 
* Open a terminal within desired directory
* run following bash command to set the initial database

python ../sqldb.py init_db

* run the main.py file to execute the program via following bash command:

python ../main.py

* now you only need to follow the questions and instructions from the habit tracker, which are run automatically by running the main.py file

 


```python

```
