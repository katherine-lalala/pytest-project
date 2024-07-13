
class TestUser:
    token_1 = ""
    username_1 = ""

    def test_login(self):
        username = "laoma"
        password = "123456"
        token = "token"   #这个是为了做什么？

        # assert token == "token"
        TestUser.username_1 = username
        TestUser.token_1 = token

    def test_userimfo(self):
        token,username = self.test_login()
        headers = {
            "token": TestUser.token_1
        }
        assert headers["token"] == TestUser.token_1


