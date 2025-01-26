from pages.base_page import BasePage


class SingleSelectPageLocators:
    """Хранит локаторы для страницы с раскрывающемся списком."""

    # Раскрывающийся список
    select = "#id_choose_language"

    # Кнопка отправки
    button = "#submit-id-submit"

    # Результат
    result_text = "#result-text"


class SingleSelectPage(BasePage):
    """Представляет страницу с раскрывающемся списком."""

    def open(self):
        """Открывает страницу."""
        return super().open("https://www.qa-practice.com/elements/select/single_select")

    def select_option(self, option_text: str):
        """Выбирает опцию из раскрывающегося списка.

        Args:
            option_text (str): Текст опции, которую нужно выбрать.
        """
        self.page.select_option(SingleSelectPageLocators.select, label=option_text)

    def click_submit_button(self):
        """Нажимаем на кнопку отправки."""
        return super().click(SingleSelectPageLocators.button)

    def get_result_text(self) -> str:
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(SingleSelectPageLocators.button, timeout=10000)
        if self.page.is_visible(SingleSelectPageLocators.result_text):
            return (
                self.page.locator(SingleSelectPageLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
