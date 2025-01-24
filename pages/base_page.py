from playwright.sync_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        """Открывает страницу."""
        self.page.goto(url)

    def click(self, selector: str):
        """Кликает на элемент."""
        self.page.click(selector)

    def is_visible(self, selector: str) -> bool:
        """Проверяет, виден ли элемент на странице."""
        return self.page.is_visible(selector)
