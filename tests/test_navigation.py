from playwright.sync_api import Page
from pages.home_page import HomePage


def test_homepage_home_button_exist(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.check_navbar_home_button_exist()


def test_homepage_home_button_click(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.click_navbar_home_button()
    home_page.check_page_title_text_is_('Test home page')


def test_homepage_login_button_exist(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.check_navbar_login_button_exist()


def test_homepage_login_button_click(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.click_navbar_login_button()
    home_page.check_page_title_text_is_('Login')


def test_homepage_signup_button_exist(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.check_navbar_signup_button_exist()


def test_homepage_signup_button_click(page: Page):
    home_page = HomePage(page)
    home_page.open()
    home_page.click_navbar_signup_button()
    home_page.check_page_title_text_is_('Sign Up')