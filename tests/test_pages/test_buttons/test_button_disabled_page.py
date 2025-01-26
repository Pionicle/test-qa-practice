from playwright.sync_api import Page
import pytest
import allure

from pages.buttons.button_disabled_page import DisabledButtonPage


@allure.feature("Buttons")
@allure.title("Нажатие на неактивную кнопку")
@allure.description("Тест проверяет нажатие на неактивную кнопку и результат.")
@pytest.mark.parametrize(
    "enable_button, click_button, result",
    [
        (
            False,
            True,
            "Submitted",
        ),
        (
            True,
            False,
            "",
        ),
    ],
)
def test_single_checkbox(
    page: Page,
    enable_button: bool,
    click_button: bool,
    result: str,
):
    """Тест проверяет функциональность неактивной кнопки.

    Args:
        page (Page): Объект страницы Playwright.
        enable_button (bool): Указывает, должна ли кнопка быть активной (включенной).
        click_button (bool): Указывает, следует ли нажимать на кнопку.
        result (str): Ожидаемый текст результата после нажатия на кнопку.
    """
    disabled_button_page = DisabledButtonPage(page)
    with allure.step("Открываем страницу"):
        disabled_button_page.open()

    with allure.step("Переключаем состояние кнопки"):
        disabled_button_page.switch_button(enable_button)

    with allure.step("Нажимаем на кнопку"):
        if click_button:
            disabled_button_page.click_button()

    with allure.step("Проверяем результат"):
        assert disabled_button_page.get_result_text() == result
