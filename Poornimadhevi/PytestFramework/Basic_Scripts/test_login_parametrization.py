import pytest

from input_data import *

@pytest.mark.parametrize("username, password", [('user1', 'pass1'), ('user2', 'user@123'),
                                               ('user3', 'pass@123'), ('user4', 'admin@123')])
def test_login(username, password):
    users_cred = [('user1', 'pass1'), ('user2', 'user@123'), ('user3', 'pass@1234'), ('user5', 'admin@123')]
    print("username :", username)
    print("password  :", password)
    assert (username, password) in users_cred



@pytest.mark.parametrize("username, password", users_credentials)
def test_login2(username, password):
    print("username :", username)
    print("password  :", password)
    assert (username, password) in database_cred
