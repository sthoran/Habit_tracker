import identity_class
import sys
import datetime
import pandas as pd


class ana_habits(identity_class.identity):
    """ class including all functions related to analysis of habits. Inherits from identityClass.identity"""
    def __init__(self, username, password):
        identity_class.identity.__init__(self, username, password)
        self.currentDate = pd.to_datetime(datetime.date.today().strftime("%Y-%m-%d"))


    def streak_per_habit(self, testing=False, habit=None):
        """user specifies a habit and the longest streak for this habit will be returned
        :return: an integer representing the longest streak for given habit
        """
        if testing:
            pass # no request from user
        else:
            habit = input("Please enter your habit for which you ask for the longest streak: \t").lower()
            while habit not in self.df['habit'].unique():
                print(f'Ups! Your habit can not be found, please retry typing your habit or press "q" to quit.')
                habit = input()
                if habit == 'q':
                    return habit  
        while habit not in self.df_user['habit'].unique():
            print(habit)
            print(self.df_user['habit'].unique())
            habit = input("That habit could not be found. Please try again or use 'q' to quit: \t").lower()
            if habit == 'q':
                return habit 
        period = self.df_user[self.df_user['habit'] == habit].reset_index(drop=True)['period'][0]
        longest_streak, _ = self.get_longest_streak(
            self.df_user[self.df_user['habit'] == habit]['check_off'],  # send only timetable of given habit
            self.df_user[self.df_user['habit'] == habit].reset_index(drop=True)['period'][0])
        # print(f'Your longest streak for {habit} is {longest_streak} {period}.')
        # return nothing if user wants to keep going
        # return 0
        return habit, longest_streak, period
    

    def analysis_all_habits(self):
        """In order to filter for all habits and their respective periodicity it is assumed that
        one habit can not have 2 different periodicity.
        :returns: a dictionary of habit with respective longest streak, struggles
        """
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
            longest_streak, struggles = self.get_longest_streak(self.df_user[self.df_user['habit'] == key]['check_off'], value)
            habit_dict[key] = {
                'periodicity': value,
                'get_longest_streak': longest_streak,
                'struggles': struggles
            }
        return habit_dict
        #     table = pd.DataFrame(habit_dict)
        # print(table)


    def get_longest_streak(self, list_of_datetimes, periodicity):
        """ streak starts at 1, because with 2 repititions the streak shall be "3"
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
                if allowed_delta <= timedelta.days < upper_threshold:
                    cur_longest_streak += 1
                    if cur_longest_streak > longest_streak:
                        longest_streak = cur_longest_streak
                else:
                    struggles = self.get_struggles(list_of_datetimes, allowed_delta)
                    cur_longest_streak = 1
        return longest_streak, struggles


    def get_struggles(self, list_of_datetimes, allowed_delta):
        """ Goes through all check_off entries of user for each habit, calculates time difference (days, weeks or months)
        between each entry. Additionally also calculates the difference between today (self.currentDate) and the last entry.
        The struggle is calculated from the time difference in calc_struggle().
        :returns: struggle count per habit for user
        """
        for idx, value in enumerate(list_of_datetimes):
            if idx == 0:
                continue
            else:
                diff = list_of_datetimes[idx] - list_of_datetimes[idx - 1]
                struggles = self.__calc_struggle(diff.days, allowed_delta)
        # TODO: doc
        diff = self.currentDate - list_of_datetimes.iloc[-1]
        struggles += self.__calc_struggle(diff.days, allowed_delta)
        return struggles


    def __calc_struggle(self, diff_in_days, allowed_delta):
        """ calculates the modulo of the time difference divided by the allowed time delta ( which is defined in get_longest_streak()).
        Example: Habit with daily periodicity has an allowed time difference between entries of one. To calculate the amount of struggles if multiple
        consecutive dates were not checked, there must an upper threshold, in this case 2.
        If struggles is == 0, (calc:  time difference (6 days) / allowed delta (7) = 0,86 no struggle is counted.
        if struggles <= 1, (calc: time difference (7 days) / allowed delta (7) = 1.0, one struggle is counted. (7 days time difference means 7
        consecutive dates no entry)
        if struggles > 1 AND modulo == 0, (calc: time difference (14 days)/ allowed delta (7) = 2.0 with modulo 0), two struggles are counted.
        :returns struggle counts
        """
        struggles = 0
        modulo = diff_in_days % allowed_delta
        cur_struggle = diff_in_days / allowed_delta
        if cur_struggle <= 1:
            pass
        elif cur_struggle > 1:
            if modulo == 0:
                cur_struggle -= 1
            struggles += int(cur_struggle)
        return struggles





