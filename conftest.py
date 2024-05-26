import pytest
from playwright.sync_api import sync_playwright, Playwright, Browser, Page


# @pytest.fixture()
# def page(context):
#     page: Page = context.new_page()
#     yield page

# @pytest.fixture()
# def playwright():
#     with sync_playwright() as p:
#         yield p
#
#
# @pytest.fixture()
# def browser(playwright):
#     browser = playwright.chromium.launch()
#     yield browser
#     browser.close()
#
#
# @pytest.fixture(scope="function")
# def page(browser):
#     context = browser.new_context()
#     page = context.new_page()
#     yield page
#     context.close()

@pytest.fixture()
def playwright() -> Playwright:
    with sync_playwright() as p:
        yield p


@pytest.fixture()
def browser(playwright: Playwright) -> Browser:
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Page:
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
