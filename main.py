import sys

import pandas as pd

import sqldb
import identityClass
import habitClass
import userInteraction
import analysis

#sqldb.create_table()
#con, cur = sqldb.connect_db()
#sqldb.dummy_fill_db(cur)
#sqldb.close_db(con)
#sqldb.show_db()


"""
TODO:
-unit test
-well-written README.md 
    - delete_habit function: write missing part for approval == 'n'
- function delete habit returns value approval, but approval is nowhere in main.py
- schleife zu main bauen nach jeder durchgeführen funktion einer abfrage 
- after create habit, continue funktioniert, danach nicht mehr
"""


if __name__ == '__main__':

    un, pwd = userInteraction.uia_init()  # asks for either 'register' or 'login'

    # object for classes, that are going to be used in the code
    habit = habitClass.habits(un, pwd)
    analysis = analysis.functions(un, pwd)

    userinput = userInteraction.uia_habit_or_analysis()
    """ asks for input to choose between 'maintain habit' (delete, create or check-off habit) or
    see 'analysis' (longest streak per habit, streak and break counts all habits) via uia_habit_or_analysis(),
    which returns input as userinput
    """
    while True: #repeat as long as the user does not quit the program
        if userinput == 'h':
            userinput = userInteraction.habit_maintenance()
            if userinput == 'h':
                """create and save a new habit in the database"""
                habit.create_habit()
                continue
            if userinput == 'c':
                """check off existing habits and save date in the database"""
                habit.check_off()
                continue
            if userinput == 'd':
                """delete habits irrevocable from the database"""
                habit.delete_habit()
            else:
                # abort program
                sys.exit("Goodbye!")
        # when see analysis was chosen by user via input == 'a
        elif userinput == 'a':
            userinput = userInteraction.see_results()
            if userinput == 'l':
                #call function to show longest streak of an specified habit by user
                analysis.streak_per_habit()
                continue
            elif userinput == 's':
                # call function, that return table of longest streak count and total break count of all habits of user
                habit_dict = analysis.analysis_all_habits()
                df = pd.DataFrame(habit_dict)
                print(df.T)
                continue
            else:
                #quit programm
                sys.exit("Goodbye!")
        elif userinput == 'q':
            #quit programm by user choice
            sys.exit("Goodbye!")





