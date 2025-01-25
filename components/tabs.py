from pages.base_page import BasePage
from playwright.sync_api import Locator


class TabsComponentLocators:
    """Хранит локаторы для вкладок."""

    # Список tabs на странице
    tabs = "ul.tabs li.tab a"
    active_tab = "ul.tabs li.tab.active a"


class TabsComponent(BasePage):
    """Представляет вкладки на текущей странице."""

    def get_tabs(self) -> list[Locator]:
        """Возвращает список локаторов всех вкладок.

        Returns:
            list[Locator]: Список локаторов для всех вкладок.
        """
        return self.page.locator(TabsComponentLocators.tabs).all()

    def get_tabs_links(self) -> list[str]:
        """Возвращает список ссылок всех вкладок.

        Returns:
            list[str]: Список ссылок для всех вкладок.
        """
        return [tab.get_attribute("href") for tab in self.get_tabs()]

    def click_tab(self, href_tab: str):
        """Кликает на вкладку по указанной ссылке.

        Args:
            href_tab (str): Ссылка на вкладку, на которую нужно кликнуть.
        """
        self.click(f"{TabsComponentLocators.tabs}[href='{href_tab}']")

    def is_active_tab(self, href_tab: str) -> bool:
        """Проверяет, является ли вкладка активной.

        Args:
            href_tab (str): Ссылка на вкладку, которую нужно проверить.

        Returns:
            bool: True, если вкладка активна, иначе False.
        """
        self.page.wait_for_selector(
            f"{TabsComponentLocators.active_tab}[href='{href_tab}']", timeout=10000
        )
        return self.is_visible(f"{TabsComponentLocators.active_tab}[href='{href_tab}']")
