import sys
import os
sys.path.append(os.getcwd())

from page.page_in import PageIn

import pytest

def get_data():
    return [("1323111", "12346")]


class TestLogin:
    # gg
    def setup_class(self):
        self.page_login = PageIn().get_page_login()

    def teardown_class(self):
        self.page_login.driver.quit()

    @pytest.mark.parametrize("username,pwd", get_data())
    def test_login(self, username, pwd):
        self.page_login.page_login(username, pwd)
