from playwright.async_api import Playwright
from playwright.sync_api import sync_playwright


def test1_co2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)").screenshot(path='output/test1.png')
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test1_co2(playwright)
