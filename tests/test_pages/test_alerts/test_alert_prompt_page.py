from playwright.sync_api import Page
import pytest
import allure

from pages.alerts.alert_prompt_page import AlertPromptPage


@allure.feature("Alert")
@allure.title("Вызов диалогового окна")
@allure.description(
    "Тест проверяет вызов диалогового окна и ввода туда текста, затем нажатие ok и cancel."
)
@pytest.mark.parametrize(
    "alert_text_result, click_ok, prompt, result_text",
    [
        ("Please enter some text", True, "", "You entered nothing"),
        ("Please enter some text", True, "Hello", "Hello"),
        ("Please enter some text", False, "", "You canceled the prompt"),
    ],
)
def test_alert_ok_cancel(
    page: Page,
    alert_text_result: str,
    click_ok: bool,
    prompt: str,
    result_text: str,
):
    """Тест для проверки вызова диалогового окна, ввода текста и корректности результата.

    Args:
        page (Page): Объект страницы Playwright.
        alert_text_result (str): Ожидаемый текст сообщения из диалогового окна.
        click_ok (bool): Если True, нажимаем 'OK'; если False, нажимаем 'Cancel'.
        prompt (str): Текст, который будет введен в диалоговое окно.
        result_text (str): Ожидаемый текст результата после нажатия кнопки.
    """
    alert_prompt_page = AlertPromptPage(page)
    with allure.step("Открываем страницу"):
        alert_prompt_page.open()

    with allure.step("Вызываем даилоговое окно и вводим текст"):
        alert_text = alert_prompt_page.open_and_promt_alert(click_ok, prompt)

    with allure.step("Проверяем сообщение из диалогового окна"):
        assert alert_text == alert_text_result

    with allure.step("проверяем результат"):
        assert alert_prompt_page.get_result_text() == result_text
