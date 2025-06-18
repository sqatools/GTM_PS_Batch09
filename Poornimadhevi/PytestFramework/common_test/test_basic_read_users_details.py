
def test_read_verify_user_details():
    username = 'newuser2'
    with open("usersdetails.txt", "r") as file:
        file_data = file.read()
        assert  username in file_data


def test_read_verify_non_existing_user():
    username = 'newuser15'
    with open("usersdetails.txt", "r") as file:
        file_data = file.read()
        assert username in file_data





