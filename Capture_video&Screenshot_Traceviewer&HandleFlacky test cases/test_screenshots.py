from playwright.sync_api import sync_playwright, expect, Page,Playwright
import pytest
import time
import datetime

def test_screenshots_demo(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #timestamp = str(int(time.time()))
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")

    #1.Page screenshot (Partial/Visible)
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png")

    #2. Full Screenshot
    #page.screenshot(path=f"screenshots/homepage_{timestamp}.png",full_page=True)

    #3. Element/Specific section of page screenshot
    logo = page.locator("img[alt='Tricentis Demo Web Shop']")
    logo.screenshot(path=f"screenshots/homepage_{timestamp}.png")

    #specific section
    section = page.locator(".product-grid")
    section.screenshot(path=f"screenshots/section_{timestamp}.png")



print(str(datetime.datetime.now()))
