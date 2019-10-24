import page
from base.base import Base


class PageLogin(Base):


    def page_input_element(self,method, values):
        self.base_input_element(method, values)

    def page_click_login(self,method):
        self.base_click_element(method)


    def page_login(self,username,pwd):
        self.page_input_element(page.login_username,username)
        self.page_input_element(page.login_password,pwd)
        self.page_click_login(page.login_btn)
