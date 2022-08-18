import sys
import identity_class



def uia_init():
    """ Asks for login, register or quit via input () and return values un, pwd (username, password),
     which where requested by "un, pwd = identityClass.ask_for_creds()" function.
    'question' is string presented to the user
    """
    print('Welcome to the tracker! Please insert your action: Login (l), register(r), quit(q)')
    userinput = input().lower()
    while (userinput not in ['l', 'r', 'q']):
        print('Input Letter was wrong, Please choose between Login (l), register(r), quit(q)')
        userinput = input().lower()
    if userinput == 'r' or userinput == 'l':
        un, pwd = identity_class.ask_for_creds()
        ident = identity_class.identity(un, pwd)
        if userinput == 'r':
            ident.create_ident()
        else:
            ident.login()
    elif userinput == 'q':
        sys.exit("Goodbye!")
    return un, pwd


def uia_habit_or_analysis():
    """ Ask question via input() to choose between habit maintenance (h), analysis results (a) or quitting the programm (q).
    Input has to be within (h,a,q) letters, otherwise new input required within the choice. (Wrong letter warning)
    :returns letter of answer (either h,a,q)
    """
    print('Do you want to work on your habits, like habit addition or habit check-off (h), see the analysis (a) or quit(q)?')
    userinput= input().lower()
    while (userinput not in ['h', 'a', 'q']):
        print('Input Letter was wrong, Please choose between habit addition and maintenance (h), check analysis (a) or quit(q)')
        userinput = input().lower()
    return userinput


def habit_maintenance():
    """ Ask question via input() to choose between create new habit (h), check off existing habit (c), delete habit(d) or quitting the program (q).
    Input has to be within (h,c,d,q) letters, otherwise new input required within the choice. (Wrong letter warning)
    :returns letter of answer (either h,c,d,q)
    """
    print('How do you want to continue? Would you like to create a new habit (h), check off an habit (c), delete a habit (d), or quit (q)')
    userinput = input().lower()
    while (userinput not in ['h', 'c', 'd', 'q']):
        print('Input Letter was wrong, Please choose between new habit (h), check-off habit (c), delete habit (d), or  quit(q)')
        userinput = input().lower()
    return userinput


def see_results():
    """Ask question via input() to choose between longest streak for specific habit (h), struggle and streak count for all habits(s) or
     quitting the program (q). Input has to be within (h,s,q) letters, otherwise new input required within the choice. (Wrong letter warning)
    :returns letter of answer (either h,s,q)
    """
    # questions the user which analysis to be done
    print("""Do you wanna see your results? 
    Please answer if you want to see your longest streak for a specific habit (l), your struggle and streak counts for all habits (s), or quit (q)""")
    userinput = input().lower()
    while (userinput not in ['l', 's',  'q']):
        print("""Input letter was wrong, Please choose between longest streak for a specific habit (l),
         your struggle and streak counts for all habits (s), or quit (q)""")
        userinput = input().lower()
    return userinput




