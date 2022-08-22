if __name__ == '__main__':
    from .. import sqldb
    from .. import analysis
else:
    import sqldb
    import analysis

"""maintests for habit accessability, analytics and availability
it is necessary to build up a filled database object to work with, that is done in module scope which would not be the standard approach for
production.
"""

# init and reset db
sqldb.init_db()
# local definitions
username = 'user1'
password = '123wer4!'

# mop floor, car wash, study 6 h, work out
def test_streak_per_habit_laundry():
    ana_obj = analysis.ana_habits(username, password)
    # test for habit 'laundry'
    assert ana_obj.streak_per_habit(testing=True, habit='laundry')[1] == 2
    
    
def test_streak_per_habit_study():
    ana_obj = analysis.ana_habits(username, password)
    # test for habit 'study'
    assert ana_obj.streak_per_habit(testing=True, habit='study')[1] == 14
        
    
def test_streak_per_habit_work_out():
    ana_obj = analysis.ana_habits(username, password)
    # test for habit 'work out'
    assert ana_obj.streak_per_habit(testing=True, habit='work out')[1] == 13
    
    
def test_streak_per_habit_car_wash():
    ana_obj = analysis.ana_habits(username, password)
    # test for habit 'car wash'
    assert ana_obj.streak_per_habit(testing=True, habit='wash car')[1] == 2

# To test the function analysis_all_habits() in analysis.py, only the struggles are tested, because the streak count was generated via longest_streak(), which was used and tested in 
#streak_per_habit() function.
def test_struggle_laundry():
    ana_obj = analysis.ana_habits(username, password)
    all_habits = ana_obj.analysis_all_habits()
    #test for struggle of habit 'laundry'
    assert all_habits['laundry']['struggles'] == 4
    
def test_struggle_study():
    ana_obj = analysis.ana_habits(username, password)
    all_habits = ana_obj.analysis_all_habits()
    #test for struggle of habit 'study'
    assert all_habits['study']['struggles'] == 29
    
def test_struggle_wash_car():
    ana_obj = analysis.ana_habits(username, password)
    all_habits = ana_obj.analysis_all_habits()
    #test for struggle of habit 'wash car'
    assert all_habits['wash car']['struggles'] == 2
    
def test_struggle_work_out():
    ana_obj = analysis.ana_habits(username, password)
    all_habits = ana_obj.analysis_all_habits()
    #test for struggle of habit 'work out'
    assert all_habits['work out']['struggles'] == 25