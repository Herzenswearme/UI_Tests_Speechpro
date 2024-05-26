from playwright.sync_api import Page, expect


class BasePage:
    url = None

    def __init__(self, page: Page):
        self.page = page

    def open(self):
        if self.url:
            self.page.goto(self.url)
        else:
            print('Нельзя открыть страницу без url')

    def navbar_button(self, button_text):
        return self.page.locator('.navbar-item', has_text=button_text)

    def navbar_home_button(self):
        return self.navbar_button('Home')

    def navbar_login_button(self):
        return self.navbar_button('Login')

    def navbar_signup_button(self):
        return self.navbar_button('Sign Up')

    def navbar_profile_button(self):
        return self.navbar_button('Profile')

    def navbar_logout_button(self):
        return self.navbar_button('Logout')

    def check_page_title_text_is_(self, text):
        title_text = self.page.get_by_role('heading', name=text)
        expect(title_text).to_have_text(text)

    def check_navbar_home_button_exist(self):
        navbar_home_button = self.navbar_home_button()
        expect(navbar_home_button).to_be_visible()

    def click_navbar_home_button(self):
        navbar_home_button = self.navbar_home_button()
        navbar_home_button.click()

    def check_navbar_login_button_exist(self):
        navbar_login_button = self.navbar_login_button()
        expect(navbar_login_button).to_be_visible()

    def click_navbar_login_button(self):
        navbar_login_button = self.navbar_login_button()
        navbar_login_button.click()

    def check_navbar_signup_button_exist(self):
        navbar_signup_button = self.navbar_signup_button()
        expect(navbar_signup_button).to_be_visible()

    def click_navbar_signup_button(self):
        navbar_signup_button = self.navbar_signup_button()
        navbar_signup_button.click()

    def check_navbar_profile_button_exist(self):
        navbar_profile_button = self.navbar_profile_button()
        expect(navbar_profile_button).to_be_visible()

    def click_navbar_profile_button(self):
        navbar_profile_button = self.navbar_profile_button()
        navbar_profile_button.click()

    def check_navbar_logout_button_exist(self):
        navbar_logout_button = self.navbar_logout_button()
        expect(navbar_logout_button).to_be_visible()

    def click_navbar_logout_button(self):
        navbar_logout_button = self.navbar_logout_button()
        navbar_logout_button.click()

    def check_notification_text_is_(self, text):
        notification_text = self.page.locator('.notification', has_text=text)
        expect(notification_text).to_have_text(text)