from playwright.sync_api import Page
import pytest
import allure

from components.sidebar import SidebarComponent, SidebarLocators

base_url = "https://www.qa-practice.com"


@allure.title("Переход по меню")
@allure.description(
    "Тест проверяет переход по разделам сайта, используя боковое меню (sidebar)."
)
@pytest.mark.parametrize(
    "link_selector, expected_url",
    [
        (SidebarLocators.input, f"{base_url}/elements/input/simple"),
        (SidebarLocators.buttons, f"{base_url}/elements/button/simple"),
        (SidebarLocators.checkbox, f"{base_url}/elements/checkbox/single_checkbox"),
        (SidebarLocators.select, f"{base_url}/elements/select/single_select"),
        (SidebarLocators.new_tab, f"{base_url}/elements/new_tab/link"),
        (SidebarLocators.textarea, f"{base_url}/elements/textarea/single"),
        (SidebarLocators.alerts, f"{base_url}/elements/alert/alert"),
        (SidebarLocators.dragndrop, f"{base_url}/elements/dragndrop/boxes"),
        (SidebarLocators.iframes, f"{base_url}/elements/iframe/iframe_page"),
        (SidebarLocators.pop_up, f"{base_url}/elements/popup/modal"),
    ],
)
def test_sidebar_navigation(page: Page, link_selector: str, expected_url: str):
    sidebar = SidebarComponent(page)
    with allure.step("Открываем сайт"):
        sidebar.open()

    with allure.step("Открываем меню"):
        sidebar.open_sidebar()

    with allure.step("Нажимаем на пункт меню"):
        sidebar.click(link_selector)

    assert page.url == expected_url


@allure.title("Переход по логотипу")
@allure.description(
    "Тест проверяет переход на главную страницу сайта с помощью логотипа."
)
@pytest.mark.parametrize(
    "link_selector, expected_url",
    [
        (SidebarLocators.logo, f"{base_url}/"),
    ],
)
def test_sidebar_logo(page: Page, link_selector: str, expected_url: str):
    sidebar = SidebarComponent(page)
    with allure.step("Открываем сайт"):
        sidebar.open()

    with allure.step("Нажимаем на логотип"):
        sidebar.click(link_selector)

    assert page.url == expected_url
