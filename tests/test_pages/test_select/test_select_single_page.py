from playwright.sync_api import Page
import pytest
import allure

from pages.select.select_single_page import SingleSelectPage


@allure.feature("Select")
@allure.title("Выбор опции в раскрывающемся списке")
@allure.description(
    "Тест проверяет выбор опции в раскрывающемся списке, его отправку и результат сообщения."
)
@pytest.mark.parametrize(
    "option_text, result",
    [
        ("", ""),
        ("Python", "Python"),
        ("Ruby", "Ruby"),
        ("JavaScript", "JavaScript"),
        ("Java", "Java"),
        ("C#", "C#"),
    ],
)
def test_single_select(
    page: Page,
    option_text: str,
    result: str,
):
    """Тест проверяет функциональность выбора опции в раскрывающемся списке.

    Args:
        page (Page): Объект страницы Playwright.
        option_text (str): Текст опции, которую нужно выбрать.
        result (str): Ожидаемый текст результата после отправки выбора.
    """
    simple_select_page = SingleSelectPage(page)

    with allure.step("Открываем страницу"):
        simple_select_page.open()

    with allure.step("Выбираем опцию"):
        simple_select_page.select_option(option_text)

    with allure.step("Отправляем выбор"):
        simple_select_page.click_submit_button()

    with allure.step("Результат вывода правильный"):
        assert simple_select_page.get_result_text() == result
