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

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        return super().open("https://www.qa-practice.com/elements/input/passwd")

    def fill_text_input(self, text: str):
        self.fill(InputPasswordPageLocators.text_input, text)

    def submit_text(self):
        self.page.press(InputPasswordPageLocators.text_input, key="Enter")

    def get_text_result(self) -> str:
        self.page.wait_for_selector(InputPasswordPageLocators.text_output)
        return self.page.locator(InputPasswordPageLocators.text_output).text_content()

    def get_text_error(self) -> str:
        self.page.wait_for_selector(InputPasswordPageLocators.text_error)
        return self.page.locator(InputPasswordPageLocators.text_error).text_content()
