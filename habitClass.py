import sqldb
import identityClass
import datetime
import sys
"""
TODO:
    - in create_habit function, the output is ugly and should be a table, need to change the layout.
    - in check off habit, fix insertion of duplicates
    -functions are not saved on local database and can not be called again after leaving session
"""
class habits(identityClass.identity):
    def __init__(self, username, password):
        identityClass.identity.__init__(self, username, password)
        self.currentDate = datetime.date.today().strftime("%Y-%m-%d")





    def create_habit(self):
        """
        This function gives user the opportunity to create a new habit that is stored automatically in the local database
        :return:
        """
        con, cur = sqldb.connect_db()
        habit = input("Please enter your new habit: \t")
        self.period = input("How often do you want to do your habit? daily (d), weekly (w), or monthly (m)?: \t").lower()
        check_off_date_answer = input("Did you complete your habit today? Please enter (y) or (q) for quit: \t").lower()
        while check_off_date_answer not in ['y', 'q']:
            print('Input letter was wrong, Please choose between yes (y) or quit(q)')
            if habit == 'q':
                sys.exit('Goodbye')
        if check_off_date_answer == 'y':
            tmp_date = self.currentDate
            print(f'Very good! You completed your habit {habit} at the {tmp_date}.')
        else:
            sys.exit('Goodbye')
        print(f'Awesome, your habit journey starts at {tmp_date}.')
        sql = """INSERT INTO habit(username, password, habit, period, start_date) VALUES (?,?,?,?,?)"""
        cur.execute(sql,(self.username, self.password, habit, self.period, tmp_date))
        cur.execute('SELECT DISTINCT * FROM habit WHERE username = ? AND password = ? AND habit = ?', (self.username, self.password, habit))
        print(cur.fetchall())
        con.commit()
        con.close()

    def check_off(self):
        con, cur = sqldb.connect_db()
        habit = input('Which habit, did you complete?: \t')
        check_off_date_answer = input("Did you complete your habit today? Please enter (y) or (q) for quit: \t").lower()
        while check_off_date_answer not in ['y', 'q']:
            print('Input letter was wrong, Please choose between yes (y) or quit(q)')
            if habit == 'q':
                sys.exit('Goodbye')
        if check_off_date_answer == 'y':
            tmp_date = self.currentDate
            print(f'Very good! You completed your habit {habit} at the {tmp_date}.')
        else:
            sys.exit('Goodbye')
        sql1 = """
            INSERT INTO habit (username, password, start_date, habit, period)
            SELECT DISTINCT username, password, start_date, habit, period 
            FROM habit
            WHERE username = ? AND password = ? AND habit = ?"""
        cur.execute(sql1, (self.username, self.password, habit))
        sql2 = """
            UPDATE habit 
            SET check_off = ? WHERE username= ? AND password = ? AND habit= ? AND (check_off = "" OR check_off is NULL OR check_off = 'None')
        """
        cur.execute(sql2, (tmp_date, self.username, self.password, habit))
        cur.execute('SELECT DISTINCT * FROM habit WHERE username = ? AND password = ? AND check_off = ?',(self.username, self.password, tmp_date))
        print(cur.fetchone())
        con.commit()
        con.close()

    def delete_habit(self):
        con, cur = sqldb.connect_db()
        habit = input("Which habit do you want to delete?:  \t")
        approval = input("Are you sure you want to delete your habit irreversible? Please answer with yes (y), no (n), or quit(q)")
        while approval not in ['y', 'n', 'q']:
            print('Input letter was wrong, Please choose between yes (y), no (n) or quit(q)')
            if habit == 'q':
                sys.exit('Goodbye')
        if approval == 'y':
            sql = """DELETE FROM habit WHERE username = ? AND password = ? AND habit = ?"""
            cur.execute(sql, (self.username, self.password, habit))
            print(f'You successfully deleted {habit} from your habit list.')
            con.commit()
            con.close()



