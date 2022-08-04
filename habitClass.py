from asyncio.windows_events import NULL
import sqldb
import identityClass
import datetime
import sys
import userInteraction

class habits(identityClass.identity):
    """class that includes all functions related to direct interference with database concerning habits, such as, create a new habit,
    check of an existing habit, or delete a habit from database. Inherits from identityClass.identity attributes like username and password.
    """
    def __init__(self, username, password):
        identityClass.identity.__init__(self, username, password)
        self.currentDate = datetime.date.today().strftime("%Y-%m-%d")


    def create_habit(self):
        """This function gives user the opportunity to create a new habit that is stored automatically in the local database.
        Habit and period are asked via input() functions.
        New entry is implemented in database via sql commands using sqlite3 tool
        """
        con, cur = sqldb.connect_db()
        habit = input("Please enter your new habit: \t")
        print("How often do you want to do your habit? daily (d), weekly (w), monthly (m), or quit (q)?: \t")
        period = input().lower()
        while period not in ['d', 'w', 'm', 'q']:
            print('Input letter was wrong, Please choose between daily (d), weekly (w), monthly (m),  or quit (q)')
            period = input().lower()
            if habit == 'q':
                sys.exit('Goodbye')
        start_date = self.currentDate
        sql = """INSERT INTO habit(username, password, habit, period, start_date) VALUES (?,?,?,?,?)"""
        cur.execute(sql, (self.username, self.password, habit, period, start_date))
        print(f'Your new habit {habit} will start today {self.currentDate}')
        con.commit()
        con.close()

    def check_off(self):
        """This functions asks user for habit to check off and check-off date via input() function. Input of check-off date is added to user credentials
        respectively via sqlite3."""
        con, cur = sqldb.connect_db()
        habit = input('Which habit, did you complete?: \t')
        check_off_date_answer = input("Did you complete your habit today? Please enter (y) or (q) for quit: \t").lower()
        while check_off_date_answer not in ['y', 'q']:
            print('Input letter was wrong, Please choose between yes (y) or quit(q)')
            if habit == 'q':
                sys.exit('Goodbye')
        if check_off_date_answer == 'y':
            tmp_date = self.currentDate
            sql1 = """INSERT INTO habit (username, password, start_date, habit, period)
                      SELECT DISTINCT username, password, start_date, habit, period 
                      FROM habit 
                      WHERE username = ? AND password = ? AND habit = ?"""
            cur.execute(sql1, (self.username, self.password, habit))
            sql2 = """UPDATE habit 
                      SET check_off = ? WHERE username= ? AND password = ? AND habit= ? AND (check_off = "" OR check_off is NULL OR check_off = 'None')
                    """
            cur.execute(sql2, (tmp_date, self.username, self.password, habit))
            cur.execute('SELECT DISTINCT habit, period, check_off FROM habit WHERE username = ? AND password = ? AND check_off = ?'
                        , (self.username, self.password, tmp_date))
            print(cur.fetchone())
            con.commit()
            con.close()
            print(f'Very good! You completed your habit {habit} at the {tmp_date}.')
        else:
            sys.exit('Goodbye')


    def delete_habit(self):
        """ Function deletes habit given by user from database.
        A second reassurance is asked if the deletion is intended.
        If answer is yes - irrevocable deletion is carried out
        If answer is no - return to beginning of program in main.py
        """
        con, cur = sqldb.connect_db()
        # use pandas for easier queries
        user_input = input("Which habit do you want to delete?:  \t")
        # make use of inheritence: can work directly on self.df
        while user_input not in self.df['habit'].unique():
            print(f'Ups! Your habit can not be found, please retry typing your habit or press "q" to quit.')
            user_input = input()
            if user_input == 'q':
                return user_input            
        user_input = input("Are you sure you want to delete your habit irreversible? Please answer with yes (y), no (n), or quit(q):  \t")
        while user_input not in ['y', 'n', 'q']:
            print('Input letter was wrong, Please choose between yes (y), no (n) or quit(q)')
            if user_input == 'q':
                return user_input
        if user_input == 'y':
            sql = """DELETE FROM habit WHERE username = ? AND password = ? AND habit = ?"""
            cur.execute(sql, (self.username, self.password, user_input))
            print(f'You successfully deleted {user_input} from your habit list.')
            con.commit()
            con.close()
        elif user_input == 'n':
            userInteraction.uia_habit_or_analysis()
        # return nothing if user doesn't want to quit
        return NULL



