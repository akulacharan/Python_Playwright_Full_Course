from playwright.sync_api import Page,expect,Playwright
import pytest
from loginpage import LoginPage
from homepage import HomePage

@pytest.mark.parametrize("username,password,product_name",[
    ("pavanol","test@123","Samsung galaxy s6")
])
def test_user_can_login_and_add_product_to_cart(username,password,product_name,page:Page):
    page.goto("https://www.demoblaze.com/")

    #login
    login_page = LoginPage(page)
    login_page.click_login_link()
    page.wait_for_timeout(2000)
    login_page.enter_username_password(username,password)
    page.wait_for_timeout(2000)
    login_page.click_login_button()

    #homepage
    homepage = HomePage(page)
    homepage.add_product_to_cart(product_name)
    homepage.goto_cart()






