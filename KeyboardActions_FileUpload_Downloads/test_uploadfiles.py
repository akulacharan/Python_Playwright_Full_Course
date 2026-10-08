from playwright.sync_api import sync_playwright, expect, Page
import pytest

@pytest.mark.skip
def test_upload_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading single file
    page.locator("#singleFileInput").set_input_files("Uploads/Test1.txt")
    page.locator("//button[text()='Upload Single File']").click()

    # Validation
    expect(page.locator("#singleFileStatus")).to_contain_text("Test1.txt")

    page.wait_for_timeout(4000)

def test_upload_multiplefiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #uploading multiple files
    files = ["Uploads/Test1.txt","Uploads/Test2.txt"]
    page.locator("#multipleFilesInput").set_input_files(files)
    page.locator("//button[text()='Upload Multiple Files']").click()

    # Validation
    expect(page.locator("#multipleFilesStatus")).to_contain_text("Test1.txt")
    expect(page.locator("#multipleFilesStatus")).to_contain_text("Test2.txt")

    page.wait_for_timeout(4000)