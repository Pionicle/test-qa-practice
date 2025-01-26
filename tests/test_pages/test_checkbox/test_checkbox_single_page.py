from playwright.sync_api import Page
import pytest
import allure

from pages.checkbox.checkbox_single_page import SingleCheckboxPage


@allure.feature("New tab")
@allure.feature("Checkbox")
@allure.title("Нажатие на один чекбокс")
@allure.description("Тест проверяет нажатие на один чекбокс и проверяет результат.")
@pytest.mark.parametrize(
    "active, result",
    [
        (
            True,
            "select me or not",
        ),
        (
            False,
            "",
        ),
    ],
)
def test_single_checkbox(
    page: Page,
    active: bool,
    result: str,
):
    """Тест проверяет функциональность одного чекбокса.

    Args:
        page (Page): Объект страницы Playwright.
        active (bool): Указывает, должен ли чекбокс быть активным (нажатым).
        result (str): Ожидаемый текст результата после нажатия на чекбокс.
    """
    single_checkbox_page = SingleCheckboxPage(page)
    with allure.step("Открываем страницу"):
        single_checkbox_page.open()

    with allure.step("Нажимаем на чекбокс"):
        single_checkbox_page.check_checkbox(active)

    with allure.step("Проверяем что чекбокс нажат"):
        assert single_checkbox_page.is_checked_checkbox() == active

    with allure.step("Нажимаем кнопку отправки"):
        single_checkbox_page.submit()

    with allure.step("Проверяем результат"):
        assert single_checkbox_page.get_result_text() == result
