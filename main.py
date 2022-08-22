import sys
import pandas as pd
import habit_class
import userInteraction
import analysis


if __name__ == '__main__':

    un, pwd = userInteraction.uia_init()  # asks for either 'register' or 'login'

    # object for classes, that are going to be used in the code
    habit_obj = habit_class.habits(un, pwd)
    ana_obj = analysis.ana_habits(un, pwd)
    
    userinput = '' # so that we enter the next while loop atleast 1 time
    
    """asks for input to choose between 'maintain habit' (delete, create or check-off habit) or
    see 'analysis' (longest streak per habit, streak and break counts all habits) via uia_habit_or_analysis(),
    which returns input as userinput
    """
    while userinput != 'q': #repeat as long as the user does not quit the program
        userinput = userInteraction.uia_habit_or_analysis()
        if userinput == 'h':
            userinput = userInteraction.habit_maintenance()
            if userinput == 'h':
                """create and save a new habit in the database"""
                userinput = habit_obj.create_habit()
                continue
            if userinput == 'c':
                """check off existing habits and save date in the database"""
                userinput = habit_obj.check_off()
                continue
            if userinput == 'd':
                """delete habits irrevocable from the database"""
                userinput = habit_obj.delete_habit()
            else:
                # abort program
                sys.exit("Goodbye!")
        # when see analysis was chosen by user via input == 'a
        elif userinput == 'a':
            userinput = userInteraction.see_results()
            if userinput == 'l':
                #call function to show longest streak of an specified habit by user
                habit, longest_streak, period = ana_obj.streak_per_habit()
                print(f'Your longest streak for {habit} is {longest_streak} {period}.')
                continue
            elif userinput == 's':
                # call function, that return table of longest streak count and total break count of all habits of user
                habit_dict = ana_obj.analysis_all_habits()
                df = pd.DataFrame(habit_dict)
                print(df.T)
                continue
            else:
                #quit programm
                sys.exit("Goodbye!")
        elif userinput == 'q':
            #quit programm by user choice
            sys.exit("Goodbye!")
    # if user immediately chooses 'q' after inputting login data
    sys.exit("Goodbye!")





