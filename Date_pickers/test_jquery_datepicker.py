from playwright.sync_api import sync_playwright, expect,Page

def select_date(page,target_year,target_month,target_date,is_future):
    while True:
        current_month = page.locator(".ui-datepicker-month").inner_text()
        print("Current month",current_month)
        current_year = page.locator(".ui-datepicker-year").inner_text()
        print("Current year",current_year)


        if current_month == target_month and current_year == target_year:
            break
        elif is_future == True:
            page.locator("a[title='Next']").click()  #Clicks on next button
        else:
            page.locator("a[title='Prev']").click()  #Clicks on previous button

    # selecting date from the date picker
    all_dates = page.locator(".ui-datepicker-calendar td a").all()
    for dt in all_dates:
        if dt.inner_text() == target_date:
            dt.click()



def test_jquery_datepicker(page:Page):
    # Navigate to the URL
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input = page.locator("#datepicker")

    #Aproach1
    #date_input.fill('10/03/1998')
    #expect(date_input).to_have_text("10/03/1998")

    #Aproach2
    is_future = True
    year = '2027'
    month = "September"
    date ="1"

    date_input.click()  #opens the date picker

    select_date(page,year,month,date,is_future)


    expect(date_input).to_have_value("09/01/2027")


    page.wait_for_timeout(2000)