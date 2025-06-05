import pytest


@pytest.mark.parametrize("username, password", [('user1', 'pass1'), ('user2', 'user@123'),
                                               ('user3', 'pass@123'), ('user4', 'admin@123')])
def test_login(username, password):
    print("username :", username)
    print("password  :", password)

