from playwright.sync_api import Page,expect
import re


# 1) page.get_by_alt_text()
# 2) page.get_by_text()
# 3) page.get_by_role()
# 4) page.get_by_label()
# 5) get_by_placeholder()
# 6) page.get_by_title()



def test_verify_pwlocators(page:Page):
    page.goto("https://demo.nopcommerce.com/")
    page.wait_for_timeout(2000)  #give Milli seconds

    # 1) page.get_by_alt_text()
    logo = page.get_by_alt_text("nopCommerce demo store")
    expect(logo).to_be_visible()

    # 2) page.get_by_text()
    expect(page.get_by_text("Welcome to our store")).to_be_visible()
    expect(page.get_by_text("Welcome")).to_be_visible()   # We can give partial text also
    expect(page.get_by_text(re.compile(".*Welcome.*"))).to_be_visible()   # reg expression usage

def test_verify_roles(page:Page):
    # 3) page.get_by_role()
    page.goto("https://demo.nopcommerce.com/register")
    role = page.get_by_role("heading",name="Register")
    expect(role).to_be_visible()

    # 4) page.get_by_label()
    FirstName = page.get_by_label("First name:").fill("Akula")
    LastName = page.get_by_label("Last name:").fill("Charanteja")
    LastName = page.get_by_label("Email:").fill("akulacharanteja@gmail.com")
    page.wait_for_timeout(2000)  #give Milli seconds

def test_verify_Search(page:Page):
    # 5) get_by_placeholder()
    page.goto("https://demo.nopcommerce.com/register")
    page.get_by_placeholder("Search store").fill("Apple MacBook Pro")
    page.get_by_role("button",name="Search").click()
    page.wait_for_timeout(4000)  #give Milli seconds


def test_verify_title(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    title = page.get_by_title("Home page link")
    expect(title).to_have_text("Home")


def test_verify_id(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    test_id = page.get_by_test_id("profile-name")
    expect(test_id).to_have_text("John Doe")



