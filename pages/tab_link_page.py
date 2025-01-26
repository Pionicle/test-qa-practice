from pages.base_page import BasePage
from playwright.sync_api import Page


class LinkTabPageLocators:
    """Хранит локаторы для страницы с ссылкой, открывающей новую вкладку на новой странице."""

    # Ссылка на новую вкладку
    tab_link = "#new-page-link"


class LinkTabPage(BasePage):
    """Представляет страницу с ссылкой, открывающей новую вкладку на новой странице."""

    def open(self):
        """Открывает страницу."""
        return super().open("https://www.qa-practice.com/elements/new_tab/link")

    def open_new_tab_in_new_page(self):
        """Нажимает на ссылку и ожидает открытия новой вкладки.

        Returns:
            Page: Объект новой страницы, открытой в новой вкладке.
        """
        with self.page.context.expect_page() as new_page_info:
            self.click(LinkTabPageLocators.tab_link)
        new_page = new_page_info.value
        return new_page


class NewTabPageLocators:
    """Хранит локаторы для новой страницы."""

    # Результат
    result = "#result-text"


class NewTabPage(BasePage):
    """Представляет страницу с новой вкладкой."""

    def get_result_text(self) -> str:
        """Получает текст результата с новой страницы.

        Returns:
            str: Текст, содержащийся в элементе результата.
        """
        return self.page.locator(NewTabPageLocators.result).text_content()
