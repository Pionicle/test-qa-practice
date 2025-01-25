from playwright.sync_api import Page
import pytest
import allure

from components.footer import FooterComponent, FooterLocators

base_url = "https://www.qa-practice.com"


@allure.title("Переход по ссылкам футера")
@allure.description(
    "Тест проверяет переход по разделам сайта, используя футер (footer)."
)
@pytest.mark.parametrize(
    "link_selector, expected_url",
    [
        (FooterLocators.contact, f"{base_url}/contact/"),
        (FooterLocators.whats_new, f"{base_url}/whats_new/"),
        (FooterLocators.copyright_link, f"{base_url}/"),
    ],
)
def test_footer_navigation(page: Page, link_selector: str, expected_url: str):
    sidebar = FooterComponent(page)
    with allure.step("Открываем сайт"):
        sidebar.open()

    with allure.step("Нажимаем на ссылку футера"):
        sidebar.click(link_selector)

    assert page.url == expected_url
