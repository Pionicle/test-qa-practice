from playwright.sync_api import Page


class BasePageLocators:
    """Хранит локаторы страницы."""

    # Заголовки
    title_h1 = "h1"


class BasePage:
    """Базовая страница."""

    def __init__(self, page: Page):
        """
        Инициализирует базовую страницу.

        Args:
            page (Page): Объект страницы, используемый для взаимодействия с веб-страницей.
        """
        self.page = page

    def open(self, url: str):
        """
        Открывает страницу.

        Args:
            url (str): URL страницы, которую нужно открыть.
        """
        self.page.goto(url)

    def click(self, selector: str):
        """
        Кликает на элемент.

        Args:
            selector (str): Селектор элемента, на который нужно кликнуть.
        """
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        """
        Заполняет элемент текстом.

        Args:
            selector (str): Селектор элемента, который нужно заполнить текстом.
            text (str): Текст для ввода в элемент.
        """
        self.page.fill(selector, text)

    def is_visible(self, selector: str) -> bool:
        """
        Проверяет, виден ли элемент на странице.

        Args:
            selector (str): Селектор элемента, который нужно проверить.

        Returns:
            bool: True, если элемент виден, иначе False.
        """
        return self.page.is_visible(selector)

    def get_url(self) -> str:
        """
        Возвращает ссылку страницы.

        Returns:
            str: URL текущей страницы.
        """
        return self.page.url

    def get_title_h1(self) -> str:
        """
        Возвращает текст заголовка h1.

        Returns:
            str: Текст заголовка h1 на странице.
        """
        return self.page.locator(BasePageLocators.title_h1).text_content().strip()
