from pages.base_page import BasePage


class SidebarLocators:
    """Хранит локаторы компонента."""

    # Логотип и кнопка для открытия меню
    logo = "a[href='/']"
    dropdown_button = "a[href='javascript:;']"

    # Локатор состояния меню
    menu_item = "li.has-sub.active.expand"

    # Локаторы меню
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
    """Боковое меню."""

    def open(self):
        return super().open("https://www.qa-practice.com")

    def open_sidebar(self):
        """Открывает меню."""
        if not self.is_visible(SidebarLocators.menu_item):
            self.click(SidebarLocators.dropdown_button)

    def close_sidebar(self):
        """Закрывает меню."""
        if self.is_visible(SidebarLocators.menu_item):
            self.click(SidebarLocators.dropdown_button)
