from playwright.sync_api import Page
import pytest
import allure

from pages.alerts.alert_ok_page import AlertOkPage


@allure.feature("Alert")
@allure.title("Вызов диалогового окна")
@allure.description("Тест проверяет вызов диалогового окна и нажатие на кнопку ок.")
@pytest.mark.parametrize("alert_text_result", [("I am an alert!")])
def test_alert_ok(page: Page, alert_text_result: str):
    """Тест для проверки вызова диалогового окна и корректности текста сообщения.

    Args:
        page (Page): Объект страницы Playwright.
        alert_text_result (str): Ожидаемый текст сообщения из диалогового окна.
    """
    alert_ok_page = AlertOkPage(page)
    with allure.step("Открываем страницу"):
        alert_ok_page.open()

    with allure.step("Вызываем даилоговое окно"):
        alert_text = alert_ok_page.open_and_ok_alert()

    with allure.step("Проверяем сообщение из диалогового окна"):
        assert alert_text == alert_text_result

    with allure.step("Переходим на главную страницу"):
        alert_ok_page.go_to_homepage()

    with allure.step("Проверяем результат"):
        assert alert_ok_page.get_url() == "https://www.qa-practice.com/"
