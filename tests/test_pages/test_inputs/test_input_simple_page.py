from playwright.sync_api import Page
import pytest
import allure

from pages.inputs.input_simple_page import InputSimplePage


@allure.feature("Inputs")
@allure.title("Корректный ввод и отправка текста")
@allure.description(
    "Тест проверяет правильный ввод текста, его отправку и результат сообщения."
)
@pytest.mark.parametrize(
    "text",
    [
        ("hello"),
        ("hello "),
        (" hello"),
        (" hello "),
        ("ko"),
        ("1234567891123456789212345"),
    ],
)
def test_simple_input_field(
    page: Page,
    text: str,
):
    """Тестирует корректный ввод текста.

    Args:
        page (Page): Объект страницы Playwright.
        text (str): Корректный текст для ввода.
    """
    input_page = InputSimplePage(page)

    with allure.step("Открываем страницу"):
        input_page.open()

    with allure.step("Вводим текст"):
        input_page.fill_text_input(text)

    with allure.step("Отправляем текст"):
        input_page.submit_text()

    with allure.step("Результат вывода правильный"):
        assert input_page.get_text_result() == text


@allure.feature("Inputs")
@allure.title("Неправильный ввод и отправка текста")
@allure.description(
    "Тест проверяет неправильный ввод текста, его отправку и результат сообщения."
)
@pytest.mark.parametrize(
    "text, text_error",
    [
        ("1", "Please enter 2 or more characters"),
        (
            "привет",
            "Enter a valid string consisting of letters, numbers, underscores or hyphens.",
        ),
        (
            "hello _",
            "Enter a valid string consisting of letters, numbers, underscores or hyphens.",
        ),
        (
            "ffafafafasfasfasfasfasfasfasfasfasfasf",
            "Please enter no more than 25 characters",
        ),
    ],
)
def test_error_simple_input_field(
    page: Page,
    text: str,
    text_error: str,
):
    """Тестирует неправильный ввод текста.

    Args:
        page (Page): Объект страницы Playwright.
        text (str): Неправильный текст для ввода.
        text_error (str): Ожидаемое сообщение об ошибке.
    """
    input_page = InputSimplePage(page)

    with allure.step("Открываем страницу"):
        input_page.open()

    with allure.step("Вводим текст"):
        input_page.fill_text_input(text)

    with allure.step("Отправляем текст"):
        input_page.submit_text()

    with allure.step("Выводится правильное сообщение об ошибке"):
        assert input_page.get_text_error() == text_error
