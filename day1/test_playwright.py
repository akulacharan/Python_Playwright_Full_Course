import time

from playwright.sync_api import Page,expect

## Imp to run in headed mode use the command
#pytest test_playwright.py -s -v --headed
'''
def test_verifyPageUrl(page:Page):
        page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")   # Passing Url
        expect(page).to_have_url("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")  #Expected Url

def test_verifyTitle(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")
    expect(page).to_have_title("Automation Testing Practice: PlaywrightPractice")
'''


