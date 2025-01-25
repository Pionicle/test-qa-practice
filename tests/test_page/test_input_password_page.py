from playwright.sync_api import Page
import pytest
import allure

from pages.input_password_page import InputPasswordPage


@allure.title("Корректный ввод и отправка пароля")
@allure.description(
    "Тест проверяет правильный ввод пароля, его отправку и результат сообщения."
)
@pytest.mark.parametrize(
    "text",
    [
        ("Ss13246546^"),
    ],
)
def test_password_input_field(
    page: Page,
    text: str,
):
    input_page = InputPasswordPage(page)

    with allure.step("Открываем страницу"):
        input_page.open()

    with allure.step("Вводим пароль"):
        input_page.fill_text_input(text)

    with allure.step("Отправляем пароль"):
        input_page.submit_text()

    with allure.step("Результат вывода правильный"):
        assert input_page.get_text_result() == text


@allure.title("Неправильный ввод и отправка пароля")
@allure.description(
    "Тест проверяет неправильный ввод пароля, его отправку и результат сообщения."
)
@pytest.mark.parametrize(
    "text, text_error",
    [
        ("1", "Low password complexity"),
        (
            "привет",
            "Low password complexity",
        ),
        (
            "hello _",
            "Low password complexity",
        ),
    ],
)
def test_error_password_input_field(
    page: Page,
    text: str,
    text_error: str,
):
    input_page = InputPasswordPage(page)

    with allure.step("Открываем страницу"):
        input_page.open()

    with allure.step("Вводим текст"):
        input_page.fill_text_input(text)

    with allure.step("Отправляем текст"):
        input_page.submit_text()

    with allure.step("Выводится правильное сообщение об ошибке"):
        assert input_page.get_text_error() == text_error
