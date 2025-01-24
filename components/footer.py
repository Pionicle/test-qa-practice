from pages.base_page import BasePage


class FooterLocators:
    """Хранит локаторы компонента."""

    # Локаторы
    contact = "a[href='/contact/']"
    whats_new = "a[href='/whats_new/']"
    copyright_link = "footer a[href='https://www.qa-practice.com/']"


class FooterComponent(BasePage):
    """Футер."""

    def open(self):
        return super().open("https://www.qa-practice.com")
