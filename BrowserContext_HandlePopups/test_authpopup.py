from playwright.sync_api import Page,expect,Playwright
import pytest

# Direct approach inject user login with URL
# https://the-internet.herokuapp.com/basic_auth
# https://admin:admin@the-internet.herokuapp.com/basic_auth
@pytest.mark.skip
def test_authPopup(page:Page):
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("div[class='example'] p")).to_have_text("Congratulations! You must have the proper credentials.")


# Using context - we can pass username & paswd along with the context
def test_authPopup_context(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        http_credentials={"username":"admin","password":"admin"}
    )
    page = context.new_page()
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")
    page.wait_for_load_state()
    expect(page.locator("div[class='example'] p")).to_have_text("Congratulations! You must have the proper credentials.")
    page.wait_for_timeout(2000)