from playwright.sync_api import sync_playwright, expect, Page,Playwright
import pytest

search_items = ["laptop","Gift card","smartphone","monitor"]
@pytest.mark.parametrize("item",search_items)
def test_search_item(item,page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    page.locator("#small-searchterms").fill(item)
    page.locator("input[value='Search']").click()


    #Assertion
    first_result = page.locator("h2 a").nth(0)
    expect(first_result).to_contain_text(item,ignore_case=True)