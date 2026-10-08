from playwright.sync_api import Page, expect


URL = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"


def test_playwright_practice_page_elements(page: Page) -> None:
    page.goto(URL, wait_until="domcontentloaded")
    expect(page).to_have_title("Automation Testing Practice: PlaywrightPractice")

    interactive_elements = page.locator(
        "a:visible, button:visible, input:visible, textarea:visible"
    )
    for index in range(interactive_elements.count()):
        element = interactive_elements.nth(index)
        expect(element).to_be_visible()
        if element.evaluate("element => element.tagName") != "A":
            expect(element).to_be_enabled()
            element.click(trial=True)

    page.locator("#username").fill("playwright_user")
    page.locator("#email").fill("playwright@example.com")
    page.locator("input[type='password']").fill("secure-password")
    page.locator("input[type='number']").fill("10")
    page.locator("input[type='tel']").fill("1234567890")
    page.locator("textarea").fill("Playwright practice form")
    page.locator("input[type='search']").fill("Playwright")

    checkbox = page.locator("input[type='checkbox']").first
    checkbox.check()
    expect(checkbox).to_be_checked()

    standard_shipping = page.locator("input[type='radio'][value='standard']")
    standard_shipping.check()
    expect(standard_shipping).to_be_checked()
