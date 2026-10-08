from playwright.sync_api import sync_playwright, expect,Page

def test_static_web_table(page:Page):
    # Navigate to the URL
    page.goto("https://testautomationpractice.blogspot.com/")

    #locating table
    table = page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()

    #1. count total no of rows in table
    rows = table.locator("tr")          # Equals to table[name='BookTable'] tbody tr
    expect(rows).to_have_count(7)

    row_count = rows.count()
    print("Number of rows in a table",row_count) #7

    #2. Count total no of coloums/headers in table
    columns = rows.locator("th")   # Equals to table[name='BookTable'] tbody tr th
    expect(columns).to_have_count(4)

    columns_count = columns.count()
    print("Number of columns in a table", columns_count)  #4

    #3. Read all the data from second row of table
    second_row_cells = rows.nth(1).locator("td")
    second_row_texts = second_row_cells.all_inner_texts()
    print("2nd row data ==> ", second_row_texts)          #['Learn Selenium', 'Amit', 'Selenium', '300']

    expect(second_row_cells).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

    #4. Read all the data from table (Excluding header)
    all_row_data = rows.all()
    for row in all_row_data[1:]:
        cols = row.locator("td").all_inner_texts()
        print(cols)

    #5. Print book name whose author is mukesh
    for row in all_row_data[1:]:
        author_name = row.locator("td").nth(1).inner_text()
        if author_name == "Mukesh":
            book_name = row.locator("td").nth(0).inner_text()
            print(f"{author_name} \t {book_name}")

    #6. Calculate total price of all the books
    total_price=0
    all_row_data = rows.all()
    for row in all_row_data[1:]:
        prices = row.locator("td").nth(3).inner_text()
        total_price = total_price + int(prices)
    print("Total price :",total_price)








    page.wait_for_timeout(2000)