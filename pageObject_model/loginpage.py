from playwright.sync_api import Page,expect,Playwright
import pytest

class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.login_link = page.locator("#login2")
        self.username = self.page.locator("#loginusername")
        self.password = self.page.locator("#loginpassword")
        self.login_button = self.page.locator("button[onclick='logIn()']")

    def click_login_link(self):
        self.login_link.click()


    def enter_username_password(self,username,password):
        self.username.fill("")
        self.username.fill(username)
        self.password.fill("")
        self.password.fill(password)

    def click_login_button(self):
        self.login_button.click()
