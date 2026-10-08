from playwright.sync_api import sync_playwright, expect,Page

def test_bootstrapdropdown(page:Page):
    # Navigate to the URL
    page.goto("https://demowebshop.tricentis.com/")
    products = page.locator(".product-title")

    #1) inner_text() vs text_content()
    print("Using inner_text() ==>",products.nth(1).inner_text())      # returns actual text
    print("Using text_content() ==>",products.nth(1).text_content())  # returns content with special chars and spaces

    #2) all_inner_texts() vs all_text_contents()
    #product_names = products.all_text_contents()
    product_names = products.all_inner_texts()
    print(product_names)

    #3) all()   it will convert the locator object to a list object
    product_locators = products.all()
    print(product_locators[0].inner_text())

    page.wait_for_timeout(4000)