from playwright.sync_api import sync_playwright, expect, Page,Playwright
import pytest


def test_Rerun_test(page:Page):
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page.locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Wlcome pavanol') #Welcome

'''
    run using the command to run the test 3 times if it's failing
    "--headed --reruns 3 --reruns-delay 2"
'''
