from playwright.sync_api import sync_playwright, expect, Page
import pytest


def test_inner_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("Number of frames:",len(frames))  #7

    # frame3
    frame3 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")
    frame3.locator("input[name='mytext3']").fill("Welcome")

    child_frames = frame3.child_frames
    print("Number of child frames inside frame 3:",len(child_frames))

    innerframe = child_frames[0]
    radio = innerframe.get_by_label(text="I am a human")
    radio.check()

    expect(radio).to_be_checked()


    #frame5
    frame5 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_5")
    frame5.locator("input[name='mytext5']").fill("Welcome")
    frame5.locator("a[href='https://a9t9.com']").click()

    expect(frame5.get_by_alt_text("Ui.Vision by a9t9 software - Image-Driven Automation")).to_be_visible()  # to check logo



    page.wait_for_timeout(3000)