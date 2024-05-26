import time

import pytest
from pages.signup_page import SignupPage


def test_registration_without_fill_required_fields(page):
    signup_page = SignupPage(page)
    # 1. Переход на страницу регистрации
    signup_page.open()
    # 2. Нажать на кнопку зарегистрироваться
    signup_page.click_signup_form_signup_button()
    # 3. Проверить, что пользователь не зарегистрировался
    try:
        signup_page.check_page_title_text_is_('Sign Up')
    except AssertionError:
        title = page.locator('h3').text_content()  #уточнить сообщение об ошибке и изменить на проверку этого сообщения
        pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Sign Up", но был {title}')


def test_registration_without_fill_password(page):
    signup_page = SignupPage(page)
    # 1. Переход на страницу регистрации
    signup_page.open()
    # 2. Ввести email
    signup_page.fill_signup_form_email_field('test50@test.com')
    # 3. Нажать на кнопку зарегистрироваться
    signup_page.click_signup_form_signup_button()
    # 4. Проверить, что пользователь не зарегистрировался
    try:
        signup_page.check_page_title_text_is_('Sign Up')
    except AssertionError:
        title = page.locator('h3').text_content()
        pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Sign Up", но был {title}')


def test_registration_incorrect_name(page):
    signup_page = SignupPage(page)
    incorrect_name = [
        "<script>alert( 'Привет, мир!' );</script>",
        "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure d",
        " ",
        "#$%^_=+@!/?"]
    # 1. Переход на страницу регистрации
    # 2. Ввести email
    # 3. Ввести password
    # 4. Ввести name
    for index, value in enumerate(incorrect_name):
        signup_page.open()
        signup_page.fill_signup_form_email_field(f'test4{index}@test.com')
        signup_page.fill_signup_form_password_field('Test123!')
        signup_page.fill_signup_form_name_field(value)
        print(value) # отображение текущего value
        signup_page.click_signup_form_signup_button()
    # 5. Проверить, что пользователь не зарегистрировался
        try:
            signup_page.check_page_title_text_is_('Sign Up')
        except AssertionError:
            title = page.locator('h3').text_content()
            pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Sign Up", но был {title}')