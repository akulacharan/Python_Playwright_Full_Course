import os.path

from playwright.sync_api import sync_playwright, expect, Page
import pytest

def test_downloadfile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("Welcome")
    page.locator("#generateTxt").click()

    #register an event
    '''
    #Approach1
    def handle_download(download):
        download.save_as("downloads/testfile.txt")
    page.on("download",handle_download)
    '''


    #Approach2
    page.on("download",lambda download:download.save_as("downloads/testfile.txt") )

    #download file
    page.locator("#txtDownloadLink").click()
    page.wait_for_timeout(4000)

    if os.path.exists("downloads/testfile.txt"):
        print("File exist")
    else:
        print("File not exist")
