# Habit Tracker

### Habit tracker is an open source habit manifestation program. Document the habit tracking process and receive automated analysis evaluations of your successes and difficulties that accompany you on the path to the new you.

 ## <u> Features

* Terminal operated program.
* Data is stored permanently in a local database (SQLite). User has ability to change database entry by adding or deleteing habits.
* User can use three time schedules for habit tracking (daily, weekly, monthly).
* Successfully completed habits can be documented with the "check off" feature. The day of completion is documented in the database.
* User entries are secured by registration via username and user password
* Analysis of habit tracking process does include:
    1. Streak count for a user-defined habit (Streak means, longest consecutive period of successfully completed habits)
    2. Streak count and struggle count of all habits (Struggle means, longest consecutive period of not checked-off habits)


### <u> Quick Installation Guide
   

#### Download the source code

```git clone https://github.com/sthoran/OOP_habit_tracker.git```

### <u> Run instructions

* Download the source file in a directory of your choice. 
* Open cmd (OS windows)
* Go to working directory via following command

```cd OOP_habit_tracker```

* set the initial database

```python -c "import sqldb; sqldb.init_db()"```

* run the main.py file to execute the program via following bash command:

```python main.py```

* now you only need to follow the questions and instructions from the habit tracker, which are run automatically by running the main.py file

 
### <u> Using Pytest for static test

When cloning the repository you can find static tests in the package (i.e. folder) _test_. Running the native cli command *pytest* from the working directory will not work. The reason for that is pythons import mechanic: The program in development is run from "main.py" and thus it is taking the namespace *\_\_name\_\_ == \_\_main\_\_*. All modules in subfolders can import modules from the root, in which main.py resides, without specifying a relative path.

While this works inside an IDE which marks "main.py" as our starting point, it will not work with *pytest*, due to the reason that pytest does not know where to find the modules. There we need to call pytest via python:

```python -m pytest```

This will trigger pytest with normal behaviour and the static tests that are implemented.
