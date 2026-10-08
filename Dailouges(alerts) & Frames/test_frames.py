from playwright.sync_api import sync_playwright, expect, Page
import pytest


def test_frames(page:Page):
    page.goto("https://ui.vision/demo/webtest/frames/")

    frames = page.frames
    print("Number of frames:",len(frames))  #7

    #frame1
    #frame1 = page.frame("name of the frame")  # Option 3 : get the frame using frame name (we can't use herea as it does not have name)
    #frame1 = page.frame_locator("frame[src='frame_1.html']")  # Option 1 : get the frame
    frame1 = page.frame(url="https://ui.vision/demo/webtest/frames/frame_1")  # Option 2 : get the frame using url
    input_box = frame1.locator("input[name='mytext1']")
    input_box.fill("Welcome")

    expect(input_box).to_have_text("Welcome")


    page.wait_for_timeout(3000)

