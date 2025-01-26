from pages.base_page import BasePage
from playwright.sync_api import Page


class ButtonTabPageLocators:
    """Хранит локаторы для страницы с кнопкой, открывающей новую вкладку на новой странице."""

    # Кнопка на новую вкладку
    tab_button = "#new-page-button"


class ButtonTabPage(BasePage):
    """Представляет страницу с кнопкой, открывающей новую вкладку на новой странице."""

    def open(self):
        """Открывает страницу."""
        return super().open("https://www.qa-practice.com/elements/new_tab/button")

    def open_new_tab_in_new_page(self):
        """Нажимает на кнопку и ожидает открытия новой вкладки.

        Returns:
            Page: Объект новой страницы, открытой в новой вкладке.
        """
        with self.page.context.expect_page() as new_page_info:
            self.click(ButtonTabPageLocators.tab_button)
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
