from playwright.sync_api import sync_playwright, expect, Page
import pytest


def test_keyboardactions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    input = page.locator("#input1")

    #1.focus on input1
    input.focus()

    #2. provide text in the input
    page.keyboard.insert_text("Welcome")

    #3. Ctrl + A
    page.keyboard.press("Control+A")

    # 4. Ctrl + C
    page.keyboard.press("Control+C")

    #5. Press tab key two times to navigate/focus on input2
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 6. Ctrl + V
    page.keyboard.press("Control+V")

    # 7. Press tab key two times to navigate/focus on input3
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    # 8. Ctrl + V
    page.keyboard.press("Control+V")

    input2 = page.locator("#input2")
    input3 = page.locator("#input3")

    expect(input2).to_have_value("Welcome")
    expect(input3).to_have_value("Welcome")

    page.wait_for_timeout(4000)

