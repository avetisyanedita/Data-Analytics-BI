from playwright.sync_api import sync_playwright

print("Step 1: Script started")

with sync_playwright() as p:
    print("Step 2: Playwright started")

    browser = p.chromium.launch(headless=False)

    print("Step 3: Browser launched")

    page = browser.new_page()

    print("Step 4: Page created")

    page.goto("https://example.com")

    print("Step 5: Website opened")

    print(page.title())

    input("Press Enter to close...")

    browser.close()