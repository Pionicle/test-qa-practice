from pages.base_page import BasePage


class InputSimplePageLocators:
    """Хранит локаторы для страницы с простым полем ввода."""

    # Поле ввода
    text_input = "#id_text_string"

    # Поле вывода
    text_output = "#result-text"

    # Текст ошибки
    text_error = "#error_1_id_text_string"


class InputSimplePage(BasePage):
    """Представляет страницу с простым полем ввода."""

    def open(self):
        """Открывает страницу с простым полем ввода."""
        return super().open("https://www.qa-practice.com/elements/input/simple")

    def fill_text_input(self, text: str):
        """Заполняет поле ввода текстом.

        Args:
            text: Текст, который будет введен в простое поле ввода.
        """
        self.fill(InputSimplePageLocators.text_input, text)

    def submit_text(self):
        """Отправляет текст из поля ввода, нажимая клавишу Enter."""
        self.page.press(InputSimplePageLocators.text_input, key="Enter")

    def get_text_result(self) -> str:
        """Получает текст результата из поля вывода.

        Returns:
            str: Текст, отображаемый в поле вывода.
        """
        self.page.wait_for_selector(InputSimplePageLocators.text_output)
        return self.page.locator(InputSimplePageLocators.text_output).text_content()

    def get_text_error(self) -> str:
        """Получает текст ошибки из поля ошибки.

        Returns:
            str: Текст ошибки, если она отображается.
        """
        self.page.wait_for_selector(InputSimplePageLocators.text_error)
        return self.page.locator(InputSimplePageLocators.text_error).text_content()
