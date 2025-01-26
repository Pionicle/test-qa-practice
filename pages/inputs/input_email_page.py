from pages.base_page import BasePage


class InputEmailPageLocators:
    """Хранит локаторы для страницы с полем ввода для почты."""

    # Поле ввода
    text_input = "#id_email"

    # Поле вывода
    text_output = "#result-text"

    # Текст ошибки
    text_error = "#error_1_id_email"


class InputEmailPage(BasePage):
    """Представляет страницу с полем ввода для почты."""

    def open(self):
        """Открывает страницу с полем ввода для почты."""
        return super().open("https://www.qa-practice.com/elements/input/email")

    def fill_text_input(self, text: str):
        """Заполняет поле ввода текстом.

        Args:
            text: Текст, который будет введен в поле ввода.
        """
        self.fill(InputEmailPageLocators.text_input, text)

    def submit_text(self):
        """Отправляет текст из поля ввода, нажимая клавишу Enter."""
        self.page.press(InputEmailPageLocators.text_input, key="Enter")

    def get_text_result(self) -> str:
        """Получает текст результата из поля вывода.

        Returns:
            str: Текст, отображаемый в поле вывода.
        """
        self.page.wait_for_selector(InputEmailPageLocators.text_output)
        return self.page.locator(InputEmailPageLocators.text_output).text_content()

    def get_text_error(self) -> str:
        """Получает текст ошибки из поля ошибки.

        Returns:
            str: Текст ошибки, если она отображается.
        """
        self.page.wait_for_selector(InputEmailPageLocators.text_error)
        return self.page.locator(InputEmailPageLocators.text_error).text_content()
