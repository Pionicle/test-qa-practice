from pages.base_page import BasePage


class SidebarComponentLocators:
    """Хранит локаторы для бокового меню."""

    # Логотип и кнопка для открытия меню
    logo = "a[href='/']"
    dropdown_button = "a[href='javascript:;']"

    # Состояния меню
    menu_item = "li.has-sub.active.expand"

    # Элементы меню
    input = "ul.sub-menu a[href='/elements/input']"
    buttons = "ul.sub-menu a[href='/elements/button']"
    checkbox = "ul.sub-menu a[href='/elements/checkbox']"
    select = "ul.sub-menu a[href='/elements/select']"
    new_tab = "ul.sub-menu a[href='/elements/new_tab']"
    textarea = "ul.sub-menu a[href='/elements/textarea']"
    alerts = "ul.sub-menu a[href='/elements/alert']"
    dragndrop = "ul.sub-menu a[href='/elements/dragndrop']"
    iframes = "ul.sub-menu a[href='/elements/iframe/iframe_page']"
    pop_up = "ul.sub-menu a[href='/elements/popup']"


class SidebarComponent(BasePage):
    """Представляет боковое меню на сайте."""

    def open(self):
        """
        Открывает главную страницу.

        Использует метод родительского класса для перехода по URL главной страницы.
        """
        return super().open("https://www.qa-practice.com")

    def open_menu(self):
        """
        Открывает меню, если оно закрыто.

        Проверяет видимость меню и кликает на кнопку для его открытия, если меню не видно.
        """
        if not self.is_visible(SidebarComponentLocators.menu_item):
            self.click(SidebarComponentLocators.dropdown_button)

    def close_sidebar(self):
        """
        Закрывает меню, если оно открыто.

        Проверяет видимость меню и кликает на кнопку для его закрытия, если меню видно.
        """
        if self.is_visible(SidebarComponentLocators.menu_item):
            self.click(SidebarComponentLocators.dropdown_button)
