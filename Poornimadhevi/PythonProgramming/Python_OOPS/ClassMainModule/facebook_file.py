
class Facebook:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"Login Successful with credentials :{self.username}, {self.password}")


if __name__ == '__main__':
    obj = Facebook('user1@gmail.com', 'user1@12345')
    obj.login()
    print("module name :", obj.__module__)
    print("module name : ", __name__)


