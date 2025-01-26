from pages.base_page import BasePage


class LikeButtonPage:
    """Хранит локаторы для страницы с ссылкой кнопкой."""

    # Кнопка ссылка
    button = "a.a-button"

    # Результат
    result_text = "#result-text"


class SimpleButtonPage(BasePage):
    """Представляет страницу с ссылкой кнопкой."""

    def open(self):
        """Открывает страницу с ссылкой кнопкой."""
        return super().open("https://www.qa-practice.com/elements/button/like_a_button")

    def click_button(self):
        """Нажимаем на ссылку кнопку."""
        return super().click(LikeButtonPage.button)

    def get_result_text(self) -> str:
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(LikeButtonPage.button, timeout=10000)
        if self.page.is_visible(LikeButtonPage.result_text):
            return self.page.locator(LikeButtonPage.result_text).text_content().strip()
        return ""
