from playwright.async_api import Playwright
from playwright.sync_api import sync_playwright


def test2_water(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path='output/test2.png')
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test2_water(playwright)
