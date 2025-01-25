from playwright.sync_api import Page
import pytest
import allure

from pages.home_page import HomePage, HomePageLocators


@allure.title("Переход по ссылкам главной страницы")
@allure.description(
    "Тест проверяет переход по разделам сайта, используя ссылки главной страницы."
)
@pytest.mark.parametrize(
    "link_selector, expected_url, expected_title",
    [
        (
            HomePageLocators.text_input,
            "https://www.qa-practice.com/elements/input/simple",
            "Input field",
        ),
        (
            HomePageLocators.simple_button,
            "https://www.qa-practice.com/elements/button/simple",
            "Buttons",
        ),
        (
            HomePageLocators.single_checkbox,
            "https://www.qa-practice.com/elements/checkbox/single_checkbox",
            "Checkboxes",
        ),
        (
            HomePageLocators.text_area,
            "https://www.qa-practice.com/elements/textarea/single",
            "TextArea inputs",
        ),
        (
            HomePageLocators.select_input,
            "https://www.qa-practice.com/elements/select/single_select",
            "Select inputs",
        ),
    ],
)
def test_homepage_navigation(
    page: Page,
    link_selector: str,
    expected_url: str,
    expected_title: str,
):
    """
    Тест проверяет навигацию по ссылкам на главной странице.

    Args:
        page (Page): Объект страницы, используемый для взаимодействия с веб-страницей.
        link_selector (str): Селектор ссылки, по которой будет осуществлен переход.
        expected_url (str): Ожидаемый URL после перехода по ссылке.
        expected_title (str): Ожидаемый заголовок страницы после перехода.
    """
    homepage = HomePage(page)
    with allure.step("Открываем страницу"):
        homepage.open()

    with allure.step("Нажимаем на ссылку"):
        homepage.click(link_selector)

    with allure.step("Проверяем соответсвие ссылок"):
        assert homepage.get_url() == expected_url

    with allure.step("Проверяем изменение заголовка страницы"):
        assert homepage.get_title_h1() == expected_title
