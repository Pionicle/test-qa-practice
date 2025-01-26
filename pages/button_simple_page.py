from pages.base_page import BasePage


class SimpleButtonPageLocators:
    """Хранит локаторы для страницы с кнопкой."""

    # Кнопка
    button = "#submit-id-submit"

    # Результат
    result_text = "#result-text"


class SimpleButtonPage(BasePage):
    """Представляет страницу с кнопкой."""

    def open(self):
        """Открывает страницу с кнопкой."""
        return super().open("https://www.qa-practice.com/elements/button/simple")

    def click_button(self):
        """Нажимаем на кнопку."""
        return super().click(SimpleButtonPageLocators.button)

    def get_result_text(self) -> str:
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(SimpleButtonPageLocators.button, timeout=10000)
        if self.page.is_visible(SimpleButtonPageLocators.result_text):
            return (
                self.page.locator(SimpleButtonPageLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
