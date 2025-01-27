from playwright.sync_api import Page
import pytest
import allure

from pages.alerts.alert_ok_cancel_page import AlertOkCancelPage


@allure.feature("Alert")
@allure.title("Вызов диалогового окна")
@allure.description(
    "Тест проверяет вызов диалогового окна и нажатие на кнопку ок и cancel."
)
@pytest.mark.parametrize(
    "alert_text_result, click_ok, result_text",
    [
        ("Select Ok or Cancel", True, "Ok"),
        ("Select Ok or Cancel", False, "Cancel"),
    ],
)
def test_alert_ok_cancel(
    page: Page,
    alert_text_result: str,
    click_ok: bool,
    result_text: str,
):
    """Тест для проверки вызова диалогового окна и корректности текста результата.

    Args:
        page (Page): Объект страницы Playwright.
        alert_text_result (str): Ожидаемый текст сообщения из диалогового окна.
        click_ok (bool): Если True, нажимаем 'OK'; если False, нажимаем 'Cancel'.
        result_text (str): Ожидаемый текст результата после нажатия кнопки.
    """
    alert_ok_cancel_page = AlertOkCancelPage(page)
    with allure.step("Открываем страницу"):
        alert_ok_cancel_page.open()

    with allure.step("Вызываем даилоговое окно"):
        alert_text = alert_ok_cancel_page.open_and_ok_or_cancel_alert(click_ok)

    with allure.step("Проверяем сообщение из диалогового окна"):
        assert alert_text == alert_text_result

    with allure.step("проверяем результат"):
        assert alert_ok_cancel_page.get_result_text() == result_text
