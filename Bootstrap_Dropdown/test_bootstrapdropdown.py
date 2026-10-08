from playwright.sync_api import sync_playwright, expect,Page

def test_bootstrapdropdown(page:Page):
    # Navigate to the URL
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    #Login Steps
    page.locator("input[name='username']").fill("Admin")
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()

    #Click on PIM
    page.get_by_text("PIM").click()

    #Click on the Job title dropdown
    page.locator("form i").nth(2).click()
    page.wait_for_timeout(2000)

    '''Capture all the options from dropdown   
    (you can get the hidden dropdown elements by selecting the debug option in selector hub)'''

    options = page.locator("div[role='listbox'] span")
    count = options.count()
    print("Number of options in the dropdown :",count)
    expect(options).to_have_count(count)

    #Print all options
    print("All the options from the dropdown=>",options.all_text_contents())

    #Print all the options text using a loop
    for i in range(count):
        print(options.nth(i).text_content())

    # Select/Click on the specific option
    for i in range(count):
        text = options.nth(i).text_content()
        if text == "QA Engineer":
            options.nth(i).click()
            break



    page.wait_for_timeout(4000)
