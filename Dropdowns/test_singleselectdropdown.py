import pytest
from playwright.sync_api import Page, expect


def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    '''
    #3 ways to select an option Dropdown
    #Way-1
    page.locator("#country").select_option("Canada")
    page.locator("#country").select_option(label="Canada")  #by label

    #Way-2
    page.locator("#country").select_option("canada")
    page.locator("#country").select_option(value="canada")  #by value
    
    #Way-3
    page.locator("#country").select_option(index=3)         #by index, index starts from 0
    '''

    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    options_text = [text.strip() for text in dropdown_options.all_text_contents()]
    print(options_text)

    #print all the countries using loop
    for options in options_text:
        print(options)

    page.wait_for_timeout(4000)