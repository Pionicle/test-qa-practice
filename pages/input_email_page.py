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

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        return super().open("https://www.qa-practice.com/elements/input/email")

    def fill_text_input(self, text: str):
        self.fill(InputEmailPageLocators.text_input, text)

    def submit_text(self):
        self.page.press(InputEmailPageLocators.text_input, key="Enter")

    def get_text_result(self) -> str:
        self.page.wait_for_selector(InputEmailPageLocators.text_output)
        return self.page.locator(InputEmailPageLocators.text_output).text_content()

    def get_text_error(self) -> str:
        self.page.wait_for_selector(InputEmailPageLocators.text_error)
        return self.page.locator(InputEmailPageLocators.text_error).text_content()
