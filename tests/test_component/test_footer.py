from playwright.sync_api import Page
import pytest
import allure

from components.footer import FooterComponent, FooterComponentLocators


@allure.title("Переход по ссылкам футера")
@allure.description(
    "Тест проверяет переход по разделам сайта, используя футер (footer)."
)
@pytest.mark.parametrize(
    "link_selector, expected_url, expected_title",
    [
        (
            FooterComponentLocators.contact,
            "https://www.qa-practice.com/contact/",
            "Contact us",
        ),
        (
            FooterComponentLocators.whats_new,
            "https://www.qa-practice.com/whats_new/",
            "What's new",
        ),
        (
            FooterComponentLocators.copyright_link,
            "https://www.qa-practice.com/",
            "Hello!",
        ),
    ],
)
def test_footer_navigation(
    page: Page,
    link_selector: str,
    expected_url: str,
    expected_title: str,
):
    """
    Тест проверяет навигацию по ссылкам в футере сайта.

    Args:
        page (Page): Объект страницы, используемый для взаимодействия с веб-страницей.
        link_selector (str): Селектор ссылки футера, по которой будет осуществлен переход.
        expected_url (str): Ожидаемый URL после перехода по ссылке.
        expected_title (str): Ожидаемый заголовок страницы после перехода.
    """
    footer = FooterComponent(page)
    with allure.step("Открываем сайт"):
        footer.open()

    with allure.step("Нажимаем на ссылку футера"):
        footer.click(link_selector)

    with allure.step("Проверяем соответствие ссылок"):
        assert footer.get_url() == expected_url

    with allure.step("Проверяем изменение заголовка страницы"):
        assert footer.get_title_h1() == expected_title
