import identity_class

"""maintests for databse integrity, availability and accessability
"""

def test_database_not_empty():
    # Test for database availability
    username = 'user1' #correct entry
    password = '123wer4!' #correct entry
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj.df.empty # if entries are in database, than assert checks if not empty leading to a successfull test (entry is in database)
    
    
def test_user_database_not_empty():
    # Test for user database availability
    username = 'user1' #correct entry, should that be incorrect?
    password = '123wer4!' #correct entry
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj.df_user.empty # checks database only on username entries, if insert is correct and can be found in  database, it is not empty and asserted as successful
    # why not assert this function  __db_contains_un?

def test_database_request_un_pwd_correct():
    # Test with correct user and password, should work
    username = 'user1' #correct entry
    password = '123wer4!' #correct entry
    ic_obj = identity_class.identity(username, password)
    assert ic_obj._identity__db_contains_un() # if entry not in database, return false else return true. Assert is successful, if un in database is true?
    # dont understand difference between test_user_database_not_empty & test_database_request_un_pwd_correct, pwd has not been taken into consideration or has it?
    
    
def test_database_request_un_false():
    # Test with wrong user and correct password, should fail (negated assert still will be True, so that we do not see failed asserts in pytest)
    username = 'usr1' #inccorect entry
    password = '123wer4!' #correct entry
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj._identity__db_contains_un(), "Tested whether an incorrect username would fail to request database login" # here entry incorrect, so test for entry in database 
    # would return false. Meaning, that if return false assert should be successfull, is that correct? 
    
    
def test_database_request_pwd_false():
    # Test with correct user and wrong password, should fail (negated assert still will be True, so that we do not see failed asserts in pytest)
    username = 'user1'
    password = '123wr4!'
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj._identity__pwd_un_assignment_correct(), "Tested whether an incorrect password for a correct user would fail to request database login"