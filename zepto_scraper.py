# Basic example using Playwright
from playwright.sync_api import sync_playwright

def fetch_zepto_products():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.zeptonow.com/")
        page.wait_for_timeout(5000)  # wait for page to load

        # This is dummy logic. Actual selectors will depend on the website.
        product_elements = page.query_selector_all("div.product-card")
        results = []
        for el in product_elements[:10]:
            name = el.query_selector("h3").inner_text()
            price = el.query_selector(".price").inner_text()
            results.append({"name": name, "price": price})

        browser.close()
        return results
