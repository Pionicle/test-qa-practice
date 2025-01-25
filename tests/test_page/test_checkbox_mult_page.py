from playwright.sync_api import Page
import pytest
import allure

from pages.checkbox_mult_page import MultCheckboxPage


@allure.title("Нажатие на чекбоксы")
@allure.description("Тест проверяет нажатие на чекбоксы и проверяет результат.")
@pytest.mark.parametrize(
    "active, result",
    [
        (
            [True, False, False],
            "one",
        ),
        (
            [True, True, False],
            "one, two",
        ),
        (
            [True, True, True],
            "one, two, three",
        ),
        (
            [False, True, True],
            "two, three",
        ),
        (
            [False, False, True],
            "three",
        ),
        (
            [False, False, False],
            "",
        ),
    ],
)
def test_single_checkbox(
    page: Page,
    active: list[bool],
    result: str,
):
    mult_checkbox_page = MultCheckboxPage(page)
    with allure.step("Открываем страницу"):
        mult_checkbox_page.open()

    with allure.step("Нажимаем на чекбоксы"):
        mult_checkbox_page.check_checkbox(*active)

    with allure.step("Проверяем что чекбоксы нажат"):
        assert mult_checkbox_page.is_checked_checkbox() == active

    with allure.step("Нажимаем кнопку отправки"):
        mult_checkbox_page.submit()

    with allure.step("Проверяем результат"):
        assert mult_checkbox_page.get_result_text() == result
