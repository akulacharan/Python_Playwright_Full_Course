import pytest
from playwright.sync_api import Page, expect


def test_single_select_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #3 ways to select an option Dropdown
    #Way-1
    page.locator("#colors").select_option(["Blue","Yellow"])        #by label
    page.locator("#colors").select_option(label=["Blue","Yellow"])        #by label

    #Way-2
    page.locator("#colors").select_option(["blue", "green"])
    page.locator("#colors").select_option(value=["blue", "green"])   #by value

    #Way-3
    page.locator("#colors").select_option(index=[0,1])      #by index

    dropdown_options = page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)


    page.wait_for_timeout(5000)