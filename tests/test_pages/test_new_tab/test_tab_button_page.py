from playwright.sync_api import Page
import pytest
import allure

from pages.new_tab.tab_button_page import ButtonTabPage, NewTabPage


@allure.feature("New tab")
@allure.title("Открытие вкладки на новой странице")
@allure.description(
    "Тест проверяет открытие вкладки в новой странице и результат сообщения на новой странице."
)
@pytest.mark.parametrize(
    "url_new_page, result_text",
    [
        (
            "https://www.qa-practice.com/elements/new_tab/new_page",
            "I am a new page in a new tab",
        ),
    ],
)
def test_tab_button(
    page: Page,
    url_new_page: str,
    result_text: str,
):
    """Тест для проверки открытия новой вкладки и корректности текста на новой странице.

    Args:
        page (Page): Объект страницы Playwright.
        url_new_page (str): Ожидаемый URL новой страницы.
        result_text (str): Ожидаемый текст результата на новой странице.
    """

    page1 = ButtonTabPage(page)
    url_page1 = page1.get_url()

    with allure.step("Открываем страницу"):
        page1.open()

    with allure.step("Нажимаем на кнопку для открытия новой вкладки"):
        new_page = page1.open_new_tab_in_new_page()
        page2 = NewTabPage(new_page)

    with allure.step("Проверяем ссылки для 1 страницы"):
        page1.get_url() == url_page1

    with allure.step("Проверяем ссылки для 2 страницы"):
        page2.get_url() == url_new_page

    with allure.step("Результат вывода правильный"):
        assert page2.get_result_text() == result_text
