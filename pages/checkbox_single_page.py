from pages.base_page import BasePage


class SingleCheckboxPageLocators:
    """Хранит локаторы для страницы с одним чекбоксом."""

    # Чекбокс
    one_checkbox = "input[type='checkbox']#id_checkbox_0"

    # Кнопка отправки
    submit_button = "#submit-id-submit"

    # Результат
    result_text = "#result-text"


class SingleCheckboxPage(BasePage):
    """Представляет страницу с одним чекбоксом."""

    def open(self):
        """Открывает страницу с одним чекбоксом."""
        return super().open(
            "https://www.qa-practice.com/elements/checkbox/single_checkbox"
        )

    def check_checkbox(self, active: bool):
        """Устанавливает состояние чекбокса.

        Args:
            active (bool): Если True, устанавливает чекбокс; если False, снимает отметку.
        """
        if active:
            self.page.check(SingleCheckboxPageLocators.one_checkbox)
        else:
            self.page.uncheck(SingleCheckboxPageLocators.one_checkbox)

    def submit(self):
        """Кликает на кнопку отправки."""
        self.click(SingleCheckboxPageLocators.submit_button)

    def is_checked_checkbox(self) -> bool:
        """Проверяет, установлен ли чекбокс.

        Returns:
            bool: True, если чекбокс установлен, иначе False.
        """
        return self.page.is_checked(SingleCheckboxPageLocators.one_checkbox)

    def get_result_text(self) -> str:
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(SingleCheckboxPageLocators.one_checkbox)
        if self.page.is_visible(SingleCheckboxPageLocators.result_text, timeout=10000):
            return (
                self.page.locator(SingleCheckboxPageLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
