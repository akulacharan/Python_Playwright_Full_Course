from playwright.sync_api import Page,expect,Playwright
import pytest

# Browser --> Context  --> page/s

def test_popups(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()         # created context
    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com")

    #create event
    page.on("popup", lambda popup:popup.wait_for_load_state())
    page.locator("#PopUp").click()
    page.wait_for_timeout(2000)

    all_popups = context.pages
    print("Total no of pages: ",len(all_popups))

    for pw in all_popups:
        print("Pop/page URL:",pw.url)
        title = pw.title()
        if "Playwright" in title:
            print("Playwright title:",pw.title)
            pw.locator(".getStarted_Sjon").click()
            pw.wait_for_timeout(2000)
            expect(pw).to_have_title("Installation | Playwright")
            pw.close()      # Close the playwright popup window



    page.wait_for_timeout(2000)
    context.close()
    browser.close()
