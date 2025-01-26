from playwright.sync_api import Page
import pytest
import allure

from components.tabs import TabsComponent


@allure.title("Переход по ссылкам табов")
@allure.description("Тест проверяет переход по разделам сайта, используя табы.")
@pytest.mark.parametrize(
    "url_page_with_tabs",
    [
        ("https://www.qa-practice.com/elements/input/simple"),
        ("https://www.qa-practice.com/elements/button/simple"),
        ("https://www.qa-practice.com/elements/checkbox/single_checkbox"),
        ("https://www.qa-practice.com/elements/select/single_select"),
        ("https://www.qa-practice.com/elements/new_tab/link"),
        ("https://www.qa-practice.com/elements/textarea/single"),
        ("https://www.qa-practice.com/elements/alert/alert"),
        ("https://www.qa-practice.com/elements/dragndrop/boxes"),
        ("https://www.qa-practice.com/elements/iframe/iframe_page"),
        ("https://www.qa-practice.com/elements/popup/modal"),
    ],
)
def test_tabs_navigation(page: Page, url_page_with_tabs: str):
    """
    Тест проверяет навигацию по табам на текущей страницы сайта.

    Args:
        page (Page): Объект страницы Playwright.
    """
    tabs = TabsComponent(page)
    with allure.step("Открываем сайт"):
        page.goto(url_page_with_tabs)

    with allure.step("Получаем все ссылки табов"):
        tabs_links = tabs.get_tabs_links()

    with allure.step(f"Проверяем локаторы ({len(tabs_links)}) табов"):
        for index, tabs_link in enumerate(tabs_links):
            with allure.step(f"Переходим по табу {index}"):
                tabs.click_tab(tabs_link)

            with allure.step("Проверяем соответствие ссылок"):
                assert page.url == f"https://www.qa-practice.com{tabs_link}"

            with allure.step("Проверяем активен ли таб"):
                assert tabs.is_active_tab(tabs_link) == True
