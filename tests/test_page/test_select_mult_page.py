from playwright.sync_api import Page
import pytest
import allure
import random
from pages.select_mult_page import MultSelectPage


@allure.title("Выбор опций в нескольких раскрывающихся списках")
@allure.description(
    "Тест проверяет выбор опций в нескольких раскрывающихся списках, их отправку и результат сообщения."
)
@pytest.mark.parametrize("run", range(5))
def test_mult_select(page: Page, run: int):
    """Тест для проверки выбора опций в нескольких раскрывающихся списках.

    Args:
        page (Page): Объект страницы Playwright.
        run (int): Индекс текущего запуска теста.
    """
    mult_select_page = MultSelectPage(page)

    with allure.step("Открываем страницу"):
        mult_select_page.open()

    with allure.step("Выбираем опцию для списка destination"):
        options = mult_select_page.get_destination_text_options()
        destination = options[random.randint(0, len(options) - 1)]
        mult_select_page.select_destination_option(destination)

    with allure.step("Выбираем опцию для списка transport"):
        options = mult_select_page.get_transport_text_options()
        transport = options[random.randint(0, len(options) - 1)]
        mult_select_page.select_transport_option(transport)

    with allure.step("Выбираем опцию для списка when"):
        options = mult_select_page.get_when_text_options()
        when = options[random.randint(0, len(options) - 1)]
        mult_select_page.select_when_option(when)

    with allure.step("Отправляем выбор"):
        mult_select_page.click_submit_button()

    with allure.step("Результат вывода правильный"):
        if "" in [destination, transport, when]:
            assert mult_select_page.get_result_text() == ""
        else:
            assert (
                mult_select_page.get_result_text()
                == f"to go by {transport.lower()} to the {destination.lower()} {when.lower()}"
            )
