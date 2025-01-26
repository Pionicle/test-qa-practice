from pages.base_page import BasePage


class InputPasswordPageLocators:
    """Хранит локаторы для страницы с полем ввода для пароля."""

    # Поле ввода
    text_input = "#id_password"

    # Поле вывода
    text_output = "#result-text"

    # Текст ошибки
    text_error = "#error_1_id_password"


class InputPasswordPage(BasePage):
    """Представляет страницу с полем ввода для пароля."""

    def open(self):
        """Открывает страницу с полем ввода для пароля."""
        return super().open("https://www.qa-practice.com/elements/input/passwd")

    def fill_text_input(self, text: str):
        """Заполняет поле ввода пароля текстом.

        Args:
            text: Текст, который будет введен в поле ввода пароля.
        """
        self.fill(InputPasswordPageLocators.text_input, text)

    def submit_text(self):
        """Отправляет текст из поля ввода пароля, нажимая клавишу Enter."""
        self.page.press(InputPasswordPageLocators.text_input, key="Enter")

    def get_text_result(self) -> str:
        """Получает текст результата из поля вывода.

        Returns:
            str: Текст, отображаемый в поле вывода.
        """
        self.page.wait_for_selector(InputPasswordPageLocators.text_output)
        return self.page.locator(InputPasswordPageLocators.text_output).text_content()

    def get_text_error(self) -> str:
        """Получает текст ошибки из поля ошибки.

        Returns:
            str: Текст ошибки, если она отображается.
        """
        self.page.wait_for_selector(InputPasswordPageLocators.text_error)
        return self.page.locator(InputPasswordPageLocators.text_error).text_content()
