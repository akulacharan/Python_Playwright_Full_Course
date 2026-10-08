from playwright.sync_api import sync_playwright,Page



def test_login(page:Page):
    page.goto("https://tutorialsninja.com/demo/index.php?route=account/login")
    #Q: Get the url of the application into a variable and print it


    email = page.locator("input[name='email']")
    email.fill("akulacharanteja6@gmail.com")
    password = page.locator("#input-password")
    password.fill("test@123")
    page.get_by_role("button", name="Login").click()
    assert page.url == "https://tutorialsninja.com/demo/index.php?route=account/account"


    #Q: Print my account page title and url after login
'''
Generate and execute a Playwright test using pytest and Playwright MCP.
Test Scenario:
Open https://testautomationpractice.blogspot.com/p/playwrightpractice.html
verify all the elements on the page are visible and interactable.
Implementation Requirements:
Use pytest-style structure (functions starting with test_).
Execute each step interactively through Playwright MCP tools.
Once all steps succeed, generate and save the final test script as aitesting/search_product.py.
Run the saved test automatically in headed mode (browser visible).
If any step or assertion fails, identify and fix the issue, then rerun until the test passes.
Expected Output:
A fully working Playwright + pytest test script.
The script should automate the complete flow described above and successfully validate the product name in the results.
'''