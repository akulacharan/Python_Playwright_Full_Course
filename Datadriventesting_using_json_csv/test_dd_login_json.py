import json

import pytest
from playwright.sync_api import sync_playwright, expect, Page,Playwright


#import pytest


#Read json file
file = open("testdata/data.json")
login_data = json.load(file)
@pytest.mark.parametrize("email,password,validity",[
    (data['email'],data['password'],data['validity']) for data in login_data
])
def test_login_data_driven(email,password,validity,page:Page):
    page.goto("https://demowebshop.tricentis.com/login")

    # Fill login form
    page.locator("#Email").fill(email)
    page.locator("#Password").fill(password)
    page.locator('input[value="Log in"]').click()

    if validity.lower() == "valid":
        # Assert logout link visible (successful login)
        logout_link = page.locator('a[href="/logout"]')
        expect(logout_link).to_be_visible(timeout=5000)
    else:
        # Assert error message is visible (invalid login)
        error_message = page.locator(".validation-summary-errors")
        expect(error_message).to_be_visible(timeout=5000)

        # Assert user remains on login page
        expect(page).to_have_url("https://demowebshop.tricentis.com/login")

