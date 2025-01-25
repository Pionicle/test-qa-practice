from pages.base_page import BasePage


class MultCheckboxPageLocators:
    """Хранит локаторы для страницы с несколькими чекбоксоми."""

    # Чекбоксы
    one_checkbox = "input[type='checkbox']#id_checkboxes_0"
    two_checkbox = "input[type='checkbox']#id_checkboxes_1"
    three_checkbox = "input[type='checkbox']#id_checkboxes_2"

    # Кнопка отправки
    submit_button = "#submit-id-submit"

    # Результат
    result_text = "#result-text"


class MultCheckboxPage(BasePage):
    """Представляет страницу с несколькими чекбоксоми."""

    def open(self):
        """Открывает страницу с несколькими чекбоксоми."""
        return super().open(
            "https://www.qa-practice.com/elements/checkbox/mult_checkbox"
        )

    def check_checkbox(self, active_1: bool, active_2: bool, active_3: bool):
        """Устанавливает состояние чекбоксов.

        Args:
            active (bool): Если True, устанавливает чекбокс; если False, снимает отметку.
        """
        if active_1:
            self.page.check(MultCheckboxPageLocators.one_checkbox)
        else:
            self.page.uncheck(MultCheckboxPageLocators.one_checkbox)

        if active_2:
            self.page.check(MultCheckboxPageLocators.two_checkbox)
        else:
            self.page.uncheck(MultCheckboxPageLocators.two_checkbox)

        if active_3:
            self.page.check(MultCheckboxPageLocators.three_checkbox)
        else:
            self.page.uncheck(MultCheckboxPageLocators.three_checkbox)

    def submit(self):
        """Кликает на кнопку отправки."""
        self.click(MultCheckboxPageLocators.submit_button)

    def is_checked_checkbox(self) -> list[bool]:
        """Проверяет, установлены ли чекбоксы.

        Returns:
            list[bool]: True, если чекбокс установлен, иначе False.
        """
        return [
            self.page.is_checked(selector)
            for selector in [
                MultCheckboxPageLocators.one_checkbox,
                MultCheckboxPageLocators.two_checkbox,
                MultCheckboxPageLocators.three_checkbox,
            ]
        ]

    def get_result_text(self) -> str:
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(MultCheckboxPageLocators.one_checkbox)
        if self.page.is_visible(MultCheckboxPageLocators.result_text, timeout=10000):
            return (
                self.page.locator(MultCheckboxPageLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
