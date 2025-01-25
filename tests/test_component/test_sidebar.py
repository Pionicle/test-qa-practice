from playwright.sync_api import Page
import pytest
import allure

from components.sidebar import SidebarComponent, SidebarComponentLocators


@allure.title("Переход по меню")
@allure.description(
    "Тест проверяет переход по разделам сайта, используя боковое меню (sidebar)."
)
@pytest.mark.parametrize(
    "link_selector, expected_url, expected_title",
    [
        (
            SidebarComponentLocators.input,
            "https://www.qa-practice.com/elements/input/simple",
            "Input field",
        ),
        (
            SidebarComponentLocators.buttons,
            "https://www.qa-practice.com/elements/button/simple",
            "Buttons",
        ),
        (
            SidebarComponentLocators.checkbox,
            "https://www.qa-practice.com/elements/checkbox/single_checkbox",
            "Checkboxes",
        ),
        (
            SidebarComponentLocators.select,
            "https://www.qa-practice.com/elements/select/single_select",
            "Select inputs",
        ),
        (
            SidebarComponentLocators.new_tab,
            "https://www.qa-practice.com/elements/new_tab/link",
            "Open link in a new tab",
        ),
        (
            SidebarComponentLocators.textarea,
            "https://www.qa-practice.com/elements/textarea/single",
            "TextArea inputs",
        ),
        (
            SidebarComponentLocators.alerts,
            "https://www.qa-practice.com/elements/alert/alert",
            "Alerts",
        ),
        (
            SidebarComponentLocators.dragndrop,
            "https://www.qa-practice.com/elements/dragndrop/boxes",
            "Drag-n-drop",
        ),
        (
            SidebarComponentLocators.iframes,
            "https://www.qa-practice.com/elements/iframe/iframe_page",
            "Iframes",
        ),
        (
            SidebarComponentLocators.pop_up,
            "https://www.qa-practice.com/elements/popup/modal",
            "Pop-Up",
        ),
    ],
)
def test_sidebar_navigation(
    page: Page,
    link_selector: str,
    expected_url: str,
    expected_title: str,
):
    """
    Тест проверяет навигацию по пунктам меню в боковой панели.

    Args:
        page (Page): Объект страницы, используемый для взаимодействия с веб-страницей.
        link_selector (str): Селектор пункта меню, по которому будет осуществлен переход.
        expected_url (str): Ожидаемый URL после перехода по пункту меню.
        expected_title (str): Ожидаемый заголовок страницы после перехода.
    """
    sidebar = SidebarComponent(page)
    with allure.step("Открываем сайт"):
        sidebar.open()

    with allure.step("Открываем меню"):
        sidebar.open_menu()

    with allure.step("Нажимаем на пункт меню"):
        sidebar.click(link_selector)

    with allure.step("Проверяем соответствие ссылок"):
        assert sidebar.get_url() == expected_url

    with allure.step("Проверяем изменение заголовка страницы"):
        assert sidebar.get_title_h1() == expected_title


@allure.title("Переход по логотипу")
@allure.description(
    "Тест проверяет переход на главную страницу сайта с помощью логотипа."
)
@pytest.mark.parametrize(
    "link_selector, expected_url, expected_title",
    [
        (SidebarComponentLocators.logo, "https://www.qa-practice.com/", "Hello!"),
    ],
)
def test_sidebar_logo(
    page: Page,
    link_selector: str,
    expected_url: str,
    expected_title: str,
):
    """
    Тест проверяет навигацию на главную страницу через логотип в боковой панели.

    Args:
        page (Page): Объект страницы, используемый для взаимодействия с веб-страницей.
        link_selector (str): Селектор логотипа, по которому будет осуществлен переход.
        expected_url (str): Ожидаемый URL после перехода по логотипу.
        expected_title (str): Ожидаемый заголовок страницы после перехода.
    """
    sidebar = SidebarComponent(page)
    with allure.step("Открываем сайт"):
        sidebar.open()

    with allure.step("Нажимаем на логотип"):
        sidebar.click(link_selector)

    with allure.step("Проверяем соответствие ссылок"):
        assert sidebar.get_url() == expected_url

    with allure.step("Проверяем изменение заголовка страницы"):
        assert sidebar.get_title_h1() == expected_title
