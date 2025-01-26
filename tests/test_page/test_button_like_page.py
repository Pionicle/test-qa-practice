from playwright.sync_api import Page
import pytest
import allure

from pages.button_simple_page import SimpleButtonPage


@allure.title("Нажатие на кнопку ссылку")
@allure.description("Тест проверяет нажатие на кнопку ссылку и результат.")
@pytest.mark.parametrize(
    "click_button, result",
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
    click_button: bool,
    result: str,
):
    """Тест проверяет функциональность кнопки-ссылки.

    Args:
        page (Page): Объект страницы Playwright.
        click_button (bool): Указывает, следует ли нажимать на кнопку-ссылку.
        result (str): Ожидаемый текст результата после нажатия на кнопку.
    """
    simple_button_page = SimpleButtonPage(page)
    with allure.step("Открываем страницу"):
        simple_button_page.open()

    with allure.step("Нажимаем на кнопку ссылку"):
        if click_button:
            simple_button_page.click_button()

    with allure.step("Проверяем результат"):
        assert simple_button_page.get_result_text() == result
