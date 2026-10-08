from playwright.sync_api import sync_playwright, expect, Page
import pytest
import time
@pytest.mark.skip
def test_simple_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Approach1
    #Registering an event
    def handle_dialog(dialog):
        dialog.accept()
    page.on("dialog",handle_dialog)

    page.locator("#alertBtn").click()       #Clicking on button which will open dialog/alert box
    page.wait_for_timeout(4000)

@pytest.mark.skip
def test_simple_dialog2(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Approach1
    #Registering an event
    page.on("dialog",lambda dialog:dialog.accept())
    #page.pause()

    page.locator("#alertBtn").click()       #Clicking on button which will open dialog/alert box


    page.wait_for_timeout(4000)

@pytest.mark.skip
def test_conformation_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Approach1
    #Registering an event
    #page.on("dialog",lambda dialog:dialog.accept())
    page.on("dialog",lambda dialog:dialog.dismiss())
    #page.pause()
    page.wait_for_timeout(1000)
    page.locator("#confirmBtn").click()       #Clicking on button which will open dialog/alert box

    text = page.locator("#demo").inner_text()
    print("Output text==>",text)

    #expect(page.locator("#demo")).to_have_text("You pressed OK!")
    expect(page.locator("#demo")).to_have_text("You pressed Cancel!")


def test_prompt_dialog(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #Approach1
    #Registering an event
    page.on("dialog",lambda dialog:dialog.accept('Charan'))

    #page.pause()
    page.wait_for_timeout(4000)
    page.locator("#promptBtn").click()       #Clicking on button which will open dialog/alert box

    text = page.locator("#demo").inner_text()
    print("Output text==>", text)
    expect(page.locator("#demo")).to_have_text("Hello Charan! How are you today?")

    page.wait_for_timeout(5000)