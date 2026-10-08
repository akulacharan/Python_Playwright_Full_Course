"""
# Css Selectors usage

tag id                  tag#id
tag class               tag.class
tag attribute           tag[attribute=value]
tag class attribute     tag.class[attribute=value]

In all these combination tag is optional based on our requirement we can use it.
"""

from playwright.sync_api import Page,expect

def test_verify_css_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag id
    #page.locator("input#small-searchterms").fill("mobile")
    #page.locator("#small-searchterms").fill("mobile")     #also supported for a single id
    #page.wait_for_timeout(2000)


    # tag.class
    #page.locator("input.search-box-text").fill("Hello moto")
    #page.wait_for_timeout(2000)


    #tag[attribute=value]
    #page.locator("input[value='Search store']").fill("Hello")
    #page.wait_for_timeout(2000)

    #tag.class[attribute=value]
    #page.locator("input.search-box-text[value='Search store']").fill("Cherry!!")
    #page.wait_for_timeout(2000)


