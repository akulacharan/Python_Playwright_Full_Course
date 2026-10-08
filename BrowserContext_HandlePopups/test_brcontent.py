from playwright.sync_api import Page,expect,Playwright
import pytest

# Browser --> Context  --> page/s

def test_browser_context(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()         # created context

    page1 = context.new_page()  # Created page1
    page2 = context.new_page()  # Created page2

    page1.goto("https://playwright.dev/")
    page1.wait_for_timeout(3000)
    expect(page1).to_have_title("Fast and reliable end-to-end testing for modern web apps | Playwright")

    page2.goto("https://selenium.dev/")
    page2.wait_for_timeout(3000)
    expect(page2).to_have_title("Selenium")




