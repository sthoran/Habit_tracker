import sys
import sqldb
import identityClass
import habitClass
import userInteraction
import functional

sqldb.create_table()
con, cur = sqldb.connect_db()
sqldb.dummy_fill_db(cur)
sqldb.close_db(con)
sqldb.show_db()


"""
TODO:
-dokumentation (using docstrings)
-unit test
- dummy data überarbeiten
-self-contained installation and run instructions
-well-written README.md 
-cli interface
    - abfangen, dass bei leerer datenbank login möglich ist
    - check off funktion funktioniert, jedoch speichern sich die einträge nicht in die lokale datenbank langfristig
    - delete_habit function: write missing partfor approval == 'n'
    -login function: drop index from df output table
    - longest streak per habit function: print output should autocomplete d in days, w in weeks and m  in months for period value
"""



if __name__ == '__main__':

    un, pwd = userInteraction.uia_init()  # asks for either 'register' or 'login'

    # object for classes, that are going to be used in the code
    habit = habitClass.habits(un, pwd)
    analysis = functional.functions(un,pwd)
    # asks for 'maintain habit' (delete, create or check-off habit) or see 'analysis' (longest streak per habit, streak and break counts all habits)
    userinput = userInteraction.uia_habit_or_analysis()
    if userinput == 'h':
        userinput = userInteraction.habit_maintenance()
        if userinput == 'h':
            # call function to create new habit
            habit.create_habit()
        elif userinput == 'c':
            #call function to check off existing habit
            habit.check_off()
        elif userinput == 'd':
            # call function to delete existing habits
            habit.delete_habit()
        else:
            # abort programm
            sys.exit("Goodbye!")
    # when see analysis was chosen by user via input == 'a
    elif userinput == 'a':
        userinput = userInteraction.see_results()
        if userinput == 'l':
            #call function to show longest streak of an specified habit by user
            analysis.streak_per_habit()
        elif userinput == 's':
            # call function, that return table of longest streak count and total break count of all habits of user
            analysis.analysis_all_habits()
        else:
            #quit programm
            sys.exit("Goodbye!")
    elif userinput == 'q':
        #quit programm by user choice
        sys.exit("Goodbye!")






