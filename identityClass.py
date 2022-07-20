import sqldb
import pandas as pd
"""
TODO:
    - at login function, if password wrong but username right, the program does not raise an error 
"""
def ask_for_creds():
    # determines the username and password of user from input functions and returns these values
    username = input("Please enter your username: \t")
    password = input("Please enter your password: \t")
    return username, password


class identity():
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #uses input values from class and extracts username, habit and period of database from user
    def login(self):
        con, cur = sqldb.connect_db()
        #     username = input("Please enter your username: \t")
        #     password = input("Please enter your password: \t")
        print(f'Welcome {self.username}! Here is a current overview off your habits!')
        data = cur.execute('SELECT DISTINCT habit,period FROM habit WHERE username = ? AND password = ?',
                    (self.username, self.password))
        df = pd.DataFrame(data)
        print(df)
        #print(cur.fetchall())
        sqldb.close_db(con)
        # what wrong with executing function in class?
        # ident(self)

    #for new user registration
    #uses sql commands from sqlite3 to implement username and password into database
    #and returns username and password
    def create_ident(self):
        con, cur = sqldb.connect_db()
        print(self.username, self.password)
        cur.execute('INSERT INTO habit(username, password) VALUES (?, ?)', (self.username, self.password))
        cur.execute('SELECT DISTINCT username,password FROM habit WHERE username = ? AND password = ?',
                    (self.username, self.password))
        print(cur.fetchone())
        con.commit()
        con.close()

