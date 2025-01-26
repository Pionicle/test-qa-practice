from playwright.sync_api import Page
import pytest
import allure

from pages.button_simple_page import SimpleButtonPage


@allure.title("Нажатие на кнопку")
@allure.description("Тест проверяет нажатие на кнопку и результат.")
@pytest.mark.parametrize(
    "click, result",
    [
        (
            True,
            "Submitted",
        ),
        (
            False,
            "",
        ),
    ],
)
def test_single_checkbox(
    page: Page,
    click: bool,
    result: str,
):
    """Тест проверяет функциональность кнопки.

    Args:
        page (Page): Объект страницы Playwright.
        click (bool): Указывает, следует ли нажимать на кнопку.
        result (str): Ожидаемый текст результата после нажатия на кнопку.
    """
    simple_button_page = SimpleButtonPage(page)
    with allure.step("Открываем страницу"):
        simple_button_page.open()

    with allure.step("Нажимаем на кнопку"):
        if click:
            simple_button_page.click_button()

    with allure.step("Проверяем результат"):
        assert simple_button_page.get_result_text() == result
