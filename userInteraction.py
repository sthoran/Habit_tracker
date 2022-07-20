import sys
import identityClass

# class uia(identityClass.identity):
#     def __init__(self, username, password):
#         identityClass.identity.__init__(self, username, password)

def uia_init():
    print('Welcome to the tracker! Please insert your action: Login (l), register(r), quit(q)')
    userinput = input().lower()
    while (userinput not in ['l', 'r', 'q']):
        print('Input Letter was wrong, Please choose between Login (l), register(r), quit(q)')
        userinput = input().lower()
    if userinput == 'r' or userinput == 'l':
        un, pwd = identityClass.ask_for_creds()
        ident = identityClass.identity(un, pwd)
        if userinput == 'r':
            ident.create_ident()
        else:
            ident.login()
    elif userinput == 'q':
        sys.exit("Goodbye!")
    return un, pwd


def uia_habit_or_analysis():
    print('Do you want to work on your habits, like habit addition or habit check-off (h), see the analysis (a) or quit(q)?')
    userinput= input().lower()
    while (userinput not in ['h', 'a', 'q']):
        print('Input Letter was wrong, Please choose between habit addition and maintenance (h), check analysis (a) or quit(q)')
        userinput = input().lower()
    return userinput

def habit_maintenance():
    print('How do you want to continue? Would you like to create a new habit (h), check off an habit (c), delete a habit (d), or quit (q)')
    userinput = input().lower()
    while (userinput not in ['h', 'c', 'd', 'q']):
        print('Input Letter was wrong, Please choose between new habit (h), check-off habit (c), delete habit (d), or  quit(q)')
        userinput = input().lower()
    return userinput

def see_results():
    # questions the user which analysis to be done
    print('Do you wanna see your results? Please answer if you want to see your longest streak for a specific habit (l), your struggle and streak counts for all habits (s), or quit (q)')
    userinput = input().lower()
    while (userinput not in ['l', 's',  'q']):
        print('Input letter was wrong, Please choose between longest streak for a specific habit (l), your struggle and streak counts for all habits (s), or quit (q)')
        userinput = input().lower()
    return userinput



    while (userinput not in ['h', 'c', 'q']):
        print('Input Letter was wrong, Please choose between new habit (h), check-off habit (c), quit(q)')
        userinput = input().lower()
    return userinput

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
            It must be "yes" (the default), "no" or None (meaning
            an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' " "(or 'y' or 'n').\n")