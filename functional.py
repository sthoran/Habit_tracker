import sqldb
import identityClass
import pandas as pd
import sys


class functions(identityClass.identity):
    def __init__(self, username, password):
        identityClass.identity.__init__(self, username, password)
        self.df = self.__sql_to_pd()  # private functions, not interesting for anyone "outside"
        self.__clean_up_df()
        self.df_user = self.df[self.df['username'] == username]


    def __sql_to_pd(self):
        con, cur = sqldb.connect_db()
        return pd.read_sql("select * from habit", con)


    def __clean_up_df(self):
        # datatype conversion for better data transformations and aggregations
        self.df['check_off'] = pd.to_datetime(self.df['check_off'])


    def streak_per_habit(self):
        """
        user specifies a habit and the longest streak for this habit will be returned
        :return: an integer representing the longest streak for given habit
        """
        habit = input("Please enter your habit for which you ask for the longest streak: \t").lower()
        while habit not in self.df_user['habit'].unique():
            print(habit)
            print(self.df_user['habit'].unique())
            habit = input("That habit could not be found. Please try again or use 'q' to quit: \t").lower()
            if habit == 'q':
                sys.exit('Goodbye')
        period = self.df_user[self.df_user['habit'] == habit].reset_index(drop=True)['period'][0]
        longest_streak, _ = self.longest_streak(
            self.df_user[self.df_user['habit'] == habit]['check_off'],  # send only timetable of given habit
            self.df_user[self.df_user['habit'] == habit].reset_index(drop=True)['period'][0])
        print(f'Your longest streak for {habit} is {longest_streak} {period}.')
        # elif habit == 'q':
        #     sys.exit('Goodbye')


    def analysis_all_habits(self):
        '''
        In order to filter for all habits and their respective periodicity it is assumed that
        one habit can not have 2 different periodicities.
        returns a dictionary of habit with respective longest streak
        '''
        habit_dict_tmp = {}
        habit_dict = {}

        habits = self.df_user['habit'].unique()

        for habit in habits:
            # 1. get the distinct dataframe for each habit from user
            # 2. reset index to make it accessable dynamically
            # 3. choose period column out of that dataframe
            # 4. pick first row, since we're only interested in one value (i.e. 'w')
            habit_dict_tmp[habit] = self.df_user[self.df_user['habit'] == habit].reset_index(drop=True)['period'][0]

        for key, value in habit_dict_tmp.items():
            longest_streak, struggles = self.longest_streak(self.df_user[self.df_user['habit'] == key]['check_off'], value)
            habit_dict[key] = {
                'periodicity': value,
                'longest_streak': longest_streak,
                'struggles': struggles
            }
            table = pd.DataFrame(habit_dict)
        print(table)


    def longest_streak(self, list_of_datetimes, periodicity):
        """
        streak starts at 1, because with 2 repititions the streak shall be "3"
        for example:
        2021-01-20
        2021-01-21
        2021-01-22
        consecutive check offs equals to a streak of 3

        returns the longest streak of all habits as a dict
        """
        cur_longest_streak = 1
        longest_streak = 1
        biggest_struggle = 0
        # index needs reset because the series keeps index from parent dataframe
        list_of_datetimes = list_of_datetimes.reset_index(drop=True)

        if periodicity == 'd':
            allowed_delta = 1
            upper_threshold = 2
        elif periodicity == 'w':
            allowed_delta = 7
            upper_threshold = 8 # no day goodwill
        elif periodicity == 'm':
            # this approach is not 100% clean, since not every month has 28 days, also give a couple of days as goodwill
            allowed_delta = 28
            upper_threshold = 34
        for idx, value in enumerate(list_of_datetimes):
            if idx == 0:
                continue
            else:
                timedelta = list_of_datetimes[idx] - list_of_datetimes[idx - 1]
                if timedelta.days >= allowed_delta and timedelta.days < upper_threshold:

                    cur_longest_streak += 1
                    if cur_longest_streak > longest_streak:
                        longest_streak = cur_longest_streak
                else:
                    # also calculate biggest struggle streak, because it uses same logic than longest_streak
                    if timedelta.days > allowed_delta:
                        biggest_struggle += timedelta.days
                    cur_longest_streak = 1
        return longest_streak, biggest_struggle


