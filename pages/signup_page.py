from playwright.sync_api import expect
from pages.base_page import BasePage


class SignupPage(BasePage):
    url = 'http://localhost:5000/signup'

    def find_signup_form_email_placeholder(self):
        return self.page.get_by_placeholder('Email')

    def check_signup_form_email_field_exist(self):
        signup_form_email_field = self.find_signup_form_email_placeholder()
        expect(signup_form_email_field).to_be_visible()

    def fill_signup_form_email_field(self, test_email):
        return self.find_signup_form_email_placeholder().fill(test_email)

    def find_signup_form_password_placeholder(self):
        return self.page.get_by_placeholder('Password')

    def check_signup_form_password_field_exist(self):
        signup_form_password_field = self.find_signup_form_password_placeholder()
        expect(signup_form_password_field).to_be_visible()

    def fill_signup_form_password_field(self, test_password):
        return self.find_signup_form_password_placeholder().fill(test_password)

    def find_signup_form_name_placeholder(self):
        return self.page.get_by_placeholder('Name')

    def check_signup_form_name_field_exist(self):
        signup_form_password_field = self.find_signup_form_name_placeholder()
        expect(signup_form_password_field).to_be_visible()

    def fill_signup_form_name_field(self, test_password):
        return self.find_signup_form_name_placeholder().fill(test_password)

    def find_signup_form_signup_button(self):
        return self.page.get_by_role('button', name='Sign Up')

    def check_signup_form_signup_button_exist(self):
        signup_form_signup_button = self.find_signup_form_signup_button()
        expect(signup_form_signup_button).to_be_visible()

    def click_signup_form_signup_button(self):
        return self.find_signup_form_signup_button().click()