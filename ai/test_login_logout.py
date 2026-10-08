from playwright.sync_api import Page, expect

from ai.demoblaze_page import DemoBlazePage


def test_login_and_logout(page: Page) -> None:
    demoblaze = DemoBlazePage(page)
    demoblaze.open()

    expect(demoblaze.login_link).to_be_visible()
    demoblaze.open_login_dialog()
    demoblaze.login("pavanol", "test@123")

    expect(demoblaze.logout_link).to_be_visible()
    expect(demoblaze.welcome_user).to_have_text("Welcome pavanol")

    demoblaze.logout()
    expect(demoblaze.login_link).to_be_visible()
