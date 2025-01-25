from pages.base_page import BasePage


class FooterComponentLocators:
    """Хранит локаторы для футера."""

    # Локаторы
    contact = "a[href='/contact/']"
    whats_new = "a[href='/whats_new/']"
    copyright_link = "footer a[href='https://www.qa-practice.com/']"


class FooterComponent(BasePage):
    """Представляет футер на сайте."""

    def open(self):
        """
        Открывает главную страницу.

        Использует метод родительского класса для перехода по URL главной страницы.
        """
        return super().open("https://www.qa-practice.com")
