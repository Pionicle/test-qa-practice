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

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        return super().open("https://www.qa-practice.com/elements/input/simple")

    def fill_text_input(self, text: str):
        self.fill(InputSimplePageLocators.text_input, text)

    def submit_text(self):
        self.page.press(InputSimplePageLocators.text_input, key="Enter")

    def get_text_result(self) -> str:
        self.page.wait_for_selector(InputSimplePageLocators.text_output)
        return self.page.locator(InputSimplePageLocators.text_output).text_content()

    def get_text_error(self) -> str:
        self.page.wait_for_selector(InputSimplePageLocators.text_error)
        return self.page.locator(InputSimplePageLocators.text_error).text_content()
