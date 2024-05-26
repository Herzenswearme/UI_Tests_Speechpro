import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.profile_page import ProfilePage
from pages.signup_page import SignupPage
from pages.login_page import LoginPage


# Полный позитивный user flow
def test_user_flow_happyPath(page):
    home_page = HomePage(page)
    signup_page = SignupPage(page)
    login_page = LoginPage(page)
    profile_page = ProfilePage(page)

    testEmail = 'test@test.com'
    testPassword = 'testtest'
    testName = 'Test'

    # 1. Перейти на главную
    home_page.open()

    # 2. Кликнуть в меню по кнопке Sign Up
    home_page.click_navbar_signup_button()
    home_page.check_page_title_text_is_('Sign Up')

    # 3. Ввести в обязательное поле Email корректную почту
    signup_page.check_signup_form_email_field_exist()
    signup_page.fill_signup_form_email_field(testEmail)

    # 4. Ввести в обязательное поле Password корректный пароль
    signup_page.check_signup_form_password_field_exist()
    signup_page.fill_signup_form_password_field(testPassword)

    # 5. Ввести в необязательное поле Name корректное имя
    signup_page.check_signup_form_name_field_exist()
    signup_page.fill_signup_form_name_field(testName)

    # 6. Нажать в форме на кнопку Sign Up
    signup_page.check_signup_form_signup_button_exist()
    signup_page.click_signup_form_signup_button()

    # 7. Переход на страницу логина
    login_page.check_page_title_text_is_('Login')

    # 8. Ввод Email в форму логина
    login_page.check_login_form_email_field_exist()
    login_page.fill_login_form_email_field(testEmail)

    # 9. Ввод Password в форму логина
    login_page.check_login_form_password_field_exist()
    login_page.fill_login_form_password_field(testPassword)

    # 10. Выбрать чекбокс "Запомнить меня"
    login_page.check_login_form_rememberme_checkbox()
    login_page.click_login_form_rememberme_checkbox()

    # 11. Нажать на кнопку Login
    login_page.check_login_form_login_button_exist()
    login_page.click_login_form_login_button()

    # 12. Переход на страницу профиля пользователя
    profile_page.check_page_title_text_is_(f'Welcome, {testName}!')

    # 13. Нажать на кнопку Logout
    profile_page.check_navbar_logout_button_exist()
    profile_page.click_navbar_logout_button()

    # 14. Переход на страницу Home
    home_page.check_page_title_text_is_('Test home page')
    # проверить что пользователь не авторизован
    try:
        home_page.navbar_login_button().is_visible()
    except AssertionError:
        login_button_text = home_page.navbar_login_button().text_content()
        pytest.fail(f"Пользователь авторизован, кнопка {login_button_text} доступна")

# Проверка регистрации на уже зарегистрированный email
def test_registration_exist_user(page):
    testEmail = 'test1@test.com'
    testPassword = 'testtest'
    signup_page = SignupPage(page)
    login_page = LoginPage(page)
    # 1. Переход на страницу регистрации
    signup_page.open()
    # 2. Зарегистрировать пользователя
    signup_page.fill_signup_form_email_field(testEmail)
    signup_page.fill_signup_form_password_field(testPassword)
    signup_page.click_signup_form_signup_button()
    # 3. Перейти на страницу регистрации
    login_page.click_navbar_signup_button()
    # 4. Повторно зарегистрировать этого же пользователя
    signup_page.fill_signup_form_email_field(testEmail)
    signup_page.fill_signup_form_password_field(testPassword)
    signup_page.click_signup_form_signup_button()
    # 5. Проверить сообщение об ошибке
    signup_page.check_notification_text_is_('Email address already exists. Go to login page.')
    # 6. Перейти по ссылке в сообщении об ошибке
    page.get_by_role('link', name='login page').click()
    # убедиться что ссылка работает
    try:
        login_page.check_page_title_text_is_('Login')
    except AssertionError:
        title = page.locator('h3').text_content()
        pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Login", но был {title}')


# Проверка логина на незарегестрированный email
def test_login_nonexist_user(page):
    testEmail = 'test2@test.com'
    testPassword = 'testtest'
    login_page = LoginPage(page)
    # 1. Переход на страницу логина
    login_page.open()
    # 2. Ввести незарегистрированный email
    login_page.fill_login_form_email_field(testEmail)
    # 3. Ввести пароль
    login_page.fill_login_form_password_field(testPassword)
    # 4. Нажать на кнопку войти
    login_page.click_login_form_login_button()
    # 5. Проверить сообщение о наличии пользователя с таким email
    try:
        login_page.check_notification_text_is_('Please check your login details and try again.')
    except AssertionError:
        title = page.locator('h3').text_content()
        pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Login", но был {title}')


# Проверка логина с неверным паролем
def test_login_with_incorrect_password(page):
    testEmail = 'test3@test.com'
    testPassword = 'testtest'
    incorrectPassword = 'test1test'
    signup_page = SignupPage(page)
    login_page = LoginPage(page)
    # 1. Переход на страницу регистрации
    signup_page.open()
    # 2. Зарегистрировать пользователя
    signup_page.fill_signup_form_email_field(testEmail)
    signup_page.fill_signup_form_password_field(testPassword)
    signup_page.click_signup_form_signup_button()
    # 3. Войти с некорректным паролем
    login_page.fill_login_form_email_field(testEmail)
    login_page.fill_login_form_password_field(incorrectPassword)
    # 4. Нажать на кнопку войти
    login_page.click_login_form_login_button()
    # 5. Проверить сообщение об ошибке
    try:
        login_page.check_notification_text_is_('Please check your login details and try again.')
    except AssertionError:
        title = page.locator('h3').text_content()
        pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Login", но был {title}')


def test_login_with_sql_injection(page):
    testEmail = 'test4@test.com'
    testPassword = 'testtest'
    injection_pass = "' OR '1'='1'"
    signup_page = SignupPage(page)
    login_page = LoginPage(page)
    # 1. Переход на страницу регистрации
    signup_page.open()
    # 2. Зарегистрировать пользователя
    signup_page.fill_signup_form_email_field(testEmail)
    signup_page.fill_signup_form_password_field(testPassword)
    signup_page.click_signup_form_signup_button()
    # 3. Войти с некорректным паролем
    login_page.fill_login_form_email_field(testEmail)
    login_page.fill_login_form_password_field(injection_pass)
    # 4. Нажать на кнопку войти
    login_page.click_login_form_login_button()
    # 5. Проверить сообщение об ошибке
    try:
        login_page.check_notification_text_is_('Please check your login details and try again.')
    except AssertionError:
        title = page.locator('h3').text_content()
        pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Login", но был {title}')


def test_check_profile_unavailable(page):
    login_page = LoginPage(page)
    profile_page = ProfilePage(page)
    # 1. Перейти на страницу профиля
    profile_page.open()
    # 2. Переход на страницу логина с сообщением о требовании входа
    try:
        login_page.check_notification_text_is_('Please log in to access this page.')
    except AssertionError:
        title = page.locator('h3').text_content()
        pytest.fail(f'Ошибка: Ожидалось, что заголовок будет "Login", но был {title}')