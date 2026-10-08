import pytest
from playwright.sync_api import Page, expect


def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #dropdown_options = page.locator("#animals>option")      #sorted dropdown
    dropdown_options = page.locator("#colors>option")        #Unsorted dropdown

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]

    if options_text == sorted(options_text):
        print("Sorted dropdown")
        assert True
    else:
        print("Unsorted dropdown")
        assert False



