from playwright.sync_api import sync_playwright, expect, Page,Playwright
import pytest


def test_record_video(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/",
        record_video_size={"width":1024,"height":768} # This is the stand size and optional
    )
    page = context.new_page()
    page.goto('https://www.demoblaze.com/index.html')
    page.locator('#login2').click()
    page.locator('#loginusername').fill('pavanol')
    page.locator('#loginpassword').fill('test@123')
    page.locator("button:has-text('Log in')").click()
    page.wait_for_timeout(3000)

    expect(page.locator("#logout2")).to_be_visible()
    expect(page.locator('#nameofuser')).to_contain_text('Welcome pavanol')

    context.close()
    browser.close()