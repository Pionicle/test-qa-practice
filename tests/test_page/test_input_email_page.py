from playwright.sync_api import Page
import pytest
import allure

from pages.input_email_page import InputEmailPage


@allure.title("Корректный ввод и отправка почты")
@allure.description(
    "Тест проверяет правильный ввод почты, ее отправку и результат сообщения."
)
@pytest.mark.parametrize(
    "text",
    [
        ("user@example.com"),
        ("user@example.com "),
        (" user@example.com"),
        (" user@example.com "),
    ],
)
def test_email_input_field(
    page: Page,
    text: str,
):
    """Тестирует корректный ввод электронной почты.

    Args:
        page (Page): Объект страницы Playwright.
        text (str): Корректный адрес электронной почты для ввода.
    """
    input_page = InputEmailPage(page)

    with allure.step("Открываем страницу"):
        input_page.open()

    with allure.step("Вводим почту"):
        input_page.fill_text_input(text)

    with allure.step("Отправляем почту"):
        input_page.submit_text()

    with allure.step("Результат вывода правильный"):
        assert input_page.get_text_result() == text


@allure.title("Неправильный ввод и отправка почты")
@allure.description(
    "Тест проверяет неправильный ввод почты, ее отправку и результат сообщения."
)
@pytest.mark.parametrize(
    "text, text_error",
    [
        ("@example.com", "Enter a valid email address."),
        ("user@.com", "Enter a valid email address."),
        ("user@example.", "Enter a valid email address."),
        ("@example.", "Enter a valid email address."),
    ],
)
def test_error_email_input_field(
    page: Page,
    text: str,
    text_error: str,
):
    """Тестирует неправильный ввод электронной почты.

    Args:
        page (Page): Объект страницы Playwright.
        text (str): Неправильный адрес электронной почты для ввода.
        text_error (str): Ожидаемое сообщение об ошибке.
    """
    input_page = InputEmailPage(page)

    with allure.step("Открываем страницу"):
        input_page.open()

    with allure.step("Вводим почту"):
        input_page.fill_text_input(text)

    with allure.step("Отправляем почту"):
        input_page.submit_text()

    with allure.step("Выводится правильное сообщение об ошибке"):
        assert input_page.get_text_error() == text_error
