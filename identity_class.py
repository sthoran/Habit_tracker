import sqldb
import pandas as pd


def ask_for_creds():
    """
    Asks for username and password via input()
    :return: returns username, password
    """
    username = input("Please enter your username: \t")
    password = input("Please enter your password: \t")
    return username, password


class identity():
    """class that includes all functions related to the login and create identity functions.
    All direct interaction with database (such as inserts, deletion or addition is made via sql commands using sqlite3 (create_ident()).
    All analytical or visualized applications related with the database is done via pandas dataframes (login()).
    """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.df = self.__sql_to_pd()  # private functions, not interesting for anyone "outside"
        self.__clean_up_df()
        self.df_user = self.df[self.df['username'] == username]


    def __sql_to_pd(self):
        """Converts database.db in dataframe
        :returns all entries of habit datebase
        """
        con, cur = sqldb.connect_db()
        return pd.read_sql("select * from habit", con)


    def __clean_up_df(self):
        """datatype conversion for better data transformations and aggregations"""
        self.df['check_off'] = pd.to_datetime(self.df['check_off'])


    def __db_contains_un(self):
        """check for username in database
        :returns False if not available
                 True is available
        """
        if self.df_user.empty:
            return False
        else:
            return True


    def __pwd_un_assignment_correct(self):
        """check for username and password in database
         :returns False if not available in database,
                  True if available in database
        """
        if self.df_user[self.df_user['password'] == self.password].empty:
            return False
        else:
            return True


    def login(self):
        """ for user login:
        takes return value from ask_for_creds() to print unique habit and respective periodicity
        of user as table with print() statement.
        """
        while not (self.__db_contains_un() and self.__pwd_un_assignment_correct()):
            print('Your credentials were wrong! Please try again!')
            self.username, self.password = ask_for_creds()
            self.df_user = self.df[self.df['username'] == self.username]
        print(f'Welcome {self.username}! Here is a current overview off your habits!')
        for habit in self.df_user['habit'].unique():
            print(habit, self.df_user[self.df_user['habit'] == habit]['period'].reset_index(drop=True)[0])


    def create_ident(self):
        """ for new user registration:
        takes return value from ask_for_creds() to insert new entry of new user in database by using sql commands.
        """
        con, cur = sqldb.connect_db()
        print(self.username, self.password)
        cur.execute('INSERT INTO habit(username, password) VALUES (?, ?)', (self.username, self.password))
        cur.execute('SELECT DISTINCT username,password FROM habit WHERE username = ? AND password = ?',
                    (self.username, self.password))
        print(cur.fetchone())
        con.commit()
        con.close()

