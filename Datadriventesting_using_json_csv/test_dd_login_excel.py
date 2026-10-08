import pytest
from playwright.sync_api import sync_playwright, expect, Page,Playwright
import csv
import openpyxl

#reading data from excel
login_data=[]

workbook = openpyxl.load_workbook("testdata/data.xlsx")
sheet = workbook.active

#Reading data from excel sheet using for loop
for row in sheet.iter_rows(min_row=2,values_only=True):
    email,password,validity = row
    login_data.append((str(email or ""),str(password or ""), str(validity or "")))
workbook.close()


@pytest.mark.parametrize("email, password, validity",login_data)
def test_login_data_driven_excel(email,password,validity,page:Page):
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

