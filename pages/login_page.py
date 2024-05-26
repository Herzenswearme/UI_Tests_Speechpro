from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://localhost:5000/login'

    def find_login_form_email_placeholder(self):
        return self.page.get_by_placeholder('Your Email')

    def check_login_form_email_field_exist(self):
        login_form_email_field = self.find_login_form_email_placeholder()
        expect(login_form_email_field).to_be_visible()

    def fill_login_form_email_field(self, test_email):
        return self.find_login_form_email_placeholder().fill(test_email)

    def find_login_form_password_placeholder(self):
        return self.page.get_by_placeholder('Your Password')

    def check_login_form_password_field_exist(self):
        login_form_password_field = self.find_login_form_password_placeholder()
        expect(login_form_password_field).to_be_visible()

    def fill_login_form_password_field(self, test_password):
        return self.find_login_form_password_placeholder().fill(test_password)

    def find_login_form_login_button(self):
        return self.page.get_by_role('button', name='Login')

    def check_login_form_login_button_exist(self):
        login_form_login_button = self.find_login_form_login_button()
        expect(login_form_login_button).to_be_visible()

    def click_login_form_login_button(self):
        return self.find_login_form_login_button().click()

    def find_login_form_rememberme_checkbox(self):
        return self.page.get_by_role('checkbox', name='Remember me')

    def check_login_form_rememberme_checkbox(self):
        login_form_rememberme_checkbox = self.find_login_form_rememberme_checkbox()
        expect(login_form_rememberme_checkbox).to_be_visible()

    def click_login_form_rememberme_checkbox(self):
        return self.find_login_form_rememberme_checkbox().click()