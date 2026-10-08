from playwright.sync_api import Page,expect
import pytest

@pytest.mark.skip
def test_mouse_hover(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    pointme = page.locator(".dropbtn")
    pointme.hover()

    laptops = page.locator(".dropdown-content a:nth-child(2)")
    laptops.hover()

    page.wait_for_timeout(2000)

@pytest.mark.skip
def test_mouse_rightclick(page:Page):
    page.goto('https://swisnl.github.io/jQuery-contextMenu/demo.html')
    button = page.locator(".context-menu-one")
    button.click(button='right')

    page.wait_for_timeout(2000)

@pytest.mark.skip
def test_mouse_doubleclick(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    btncopy = page.locator("button[ondblclick$='myFunction1()']")
    btncopy.dblclick()

    page.wait_for_timeout(2000)


def test_mouse_draganddrop(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    source = page.locator("#draggable")
    target = page.locator("#droppable")

    #Approach1   manual drap using hover  (not recommended)
    #source.hover()
    #page.mouse.down()
    #target.hover()
    #page.mouse.up()


    #Approach2
    source.drag_to(target)

    page.wait_for_timeout(2000)