from pages.base_page import BasePage


class HomePageLocators:
    """Хранит локаторы для главной страницы."""

    # Локаторы ссылок
    text_input = "a[href='/elements/input/simple']"
    simple_button = "a[href='/elements/button/simple']"
    single_checkbox = "a[href='/elements/checkbox/single_checkbox']"
    text_area = "a[href='/elements/textarea/single']"
    select_input = "a[href='/elements/select/single_select']"


class HomePage(BasePage):
    """Представляет главную страницу сайта."""

    def open(self):
        """
        Открывает главную страницу.

        Использует метод родительского класса для перехода по URL главной страницы.
        """
        return super().open("https://www.qa-practice.com/")
