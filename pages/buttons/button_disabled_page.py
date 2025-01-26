from pages.base_page import BasePage


class DisabledButtonLocators:
    """Хранит локаторы для страницы с неактивной кнопкой."""

    # Кнопка
    button = "#submit-id-submit"

    # Перключатель состояния кнопки
    select = "#id_select_state"

    # Результат
    result_text = "#result-text"


class DisabledButtonPage(BasePage):
    """Представляет страницу с неактивной кнопкой."""

    def open(self):
        """Открывает страницу с неактивной кнопкой."""
        return super().open("https://www.qa-practice.com/elements/button/disabled")

    def switch_button(self, enable: bool):
        """Переключает состояние кнопки.

        Args:
            enable (bool): Если True, кнопка будет активной; если False, кнопка будет неактивной.
        """
        if enable:
            self.page.select_option(DisabledButtonLocators.select, "disabled")
        else:
            self.page.select_option(DisabledButtonLocators.select, "enabled")

    def click_button(self):
        """Нажимаем на кнопку."""
        return super().click(DisabledButtonLocators.button)

    def get_result_text(self) -> str:
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(DisabledButtonLocators.button, timeout=10000)
        if self.page.is_visible(DisabledButtonLocators.result_text):
            return (
                self.page.locator(DisabledButtonLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
