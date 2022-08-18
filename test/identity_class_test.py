import identity_class

"""maintests for databse integrity, availability and accessability
"""

def test_database_not_empty():
    # Test for database availability
    username = 'user1'
    password = '123wer4!'
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj.df.empty
    
    
def test_user_database_not_empty():
    # Test for user database availability
    username = 'user1'
    password = '123wer4!'
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj.df_user.empty
    

def test_database_request_un_pwd_correct():
    # Test with correct user and password, should work
    username = 'user1'
    password = '123wer4!'
    ic_obj = identity_class.identity(username, password)
    assert ic_obj._identity__db_contains_un()
    
    
def test_database_request_un_false():
    # Test with wrong user and correct password, should fail (negated assert still will be True, so that we do not see failed asserts in pytest)
    username = 'usr1'
    password = '123wer4!'
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj._identity__db_contains_un(), "Tested whether an incorrect username would fail to request database login"
    
    
def test_database_request_pwd_false():
    # Test with correct user and wrong password, should fail (negated assert still will be True, so that we do not see failed asserts in pytest)
    username = 'user1'
    password = '123wr4!'
    ic_obj = identity_class.identity(username, password)
    assert not ic_obj._identity__pwd_un_assignment_correct(), "Tested whether an incorrect password for a correct user would fail to request database login"