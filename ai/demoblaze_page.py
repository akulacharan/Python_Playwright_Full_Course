from playwright.sync_api import Page, expect


class DemoBlazePage:
    URL = "https://www.demoblaze.com/index.html"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_link = page.locator("#login2")
        self.logout_link = page.locator("#logout2")
        self.welcome_user = page.locator("#nameofuser")
        self.login_modal = page.locator("#logInModal")
        self.username = page.locator("#loginusername")
        self.password = page.locator("#loginpassword")
        self.login_button = page.locator("#logInModal button", has_text="Log in")

    def open(self) -> None:
        self.page.goto(self.URL, wait_until="domcontentloaded")

    def open_login_dialog(self) -> None:
        self.login_link.click()
        expect(self.login_modal).to_be_visible()

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
        expect(self.login_modal).to_be_hidden()

    def logout(self) -> None:
        self.logout_link.click()

