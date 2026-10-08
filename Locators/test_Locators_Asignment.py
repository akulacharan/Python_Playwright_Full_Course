from playwright.sync_api import Page,expect

def test_Orange_Login(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button",name=" Login ").click()


    expect(page.get_by_role("heading",name="Dashboard")).to_be_visible()
    page.wait_for_timeout(5000)