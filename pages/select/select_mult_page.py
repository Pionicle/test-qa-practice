from pages.base_page import BasePage


class MultSelectPageLocators:
    """Хранит локаторы для страницы с несколькими раскрывающимися спискомами."""

    # Раскрывающиеся списки
    transport_select = "#id_choose_how_you_want_to_get_there"
    destination_select = "#id_choose_the_place_you_want_to_go"
    when_select = "#id_choose_when_you_want_to_go"

    # Значения списков
    transport_value_options = "#id_choose_how_you_want_to_get_there option"
    destination_value_options = "#id_choose_the_place_you_want_to_go option"
    when_value_options = "#id_choose_when_you_want_to_go option"

    # Кнопка отправки
    button = "#submit-id-submit"

    # Результат
    result_text = "#result-text"


class MultSelectPage(BasePage):
    """Представляет страницу с несколькими раскрывающимися спискомами."""

    def open(self):
        """Открывает страницу."""
        return super().open("https://www.qa-practice.com/elements/select/mult_select")

    def _select_option(self, select_selector: str, option_text: str):
        """Выбирает опцию из раскрывающегося списка.

        Args:
            select_selector (str): селектор для раскрывающегося списка.
            option_text (str): Текст опции для выбора.
        """
        self.page.select_option(select_selector, label=option_text)

    def select_transport_option(self, option_text: str):
        """Выбирает опцию транспорта.

        Args:
            option_text (str): Текст опции транспорта для выбора.
        """
        self._select_option(MultSelectPageLocators.transport_select, option_text)

    def select_destination_option(self, option_text: str):
        """Выбирает опцию назначения.

        Args:
            option_text (str): Текст опции назначения для выбора.
        """
        self._select_option(MultSelectPageLocators.destination_select, option_text)

    def select_when_option(self, option_text: str):
        """Выбирает опцию времени.

        Args:
            option_text (str): Текст опции времени для выбора.
        """
        self._select_option(MultSelectPageLocators.when_select, option_text)

    def click_submit_button(self):
        """Нажимаем на кнопку отправки."""
        return super().click(MultSelectPageLocators.button)

    def _get_text_options(self, options_selector: str) -> list[str]:
        """Получает текст всех опций из раскрывающегося списка.

        Args:
            options_selector (str): селектор для опций.

        Returns:
            list[str]: Список текстов опций.
        """
        options = self.page.locator(options_selector).all()
        values = [option.text_content() for option in options]
        return values

    def get_transport_text_options(self) -> list[str]:
        """Получает текстовые опции транспорта.

        Returns:
            list[str]: Список текстов опций транспорта.
        """
        return self._get_text_options(MultSelectPageLocators.transport_value_options)

    def get_destination_text_options(self) -> list[str]:
        """Получает текстовые опции назначения.

        Returns:
            list[str]: Список текстов опций назначения.
        """
        return self._get_text_options(MultSelectPageLocators.destination_value_options)

    def get_when_text_options(self) -> list[str]:
        """Получает текстовые опции времени.

        Returns:
            list[str]: Список текстов опций времени.
        """
        return self._get_text_options(MultSelectPageLocators.when_value_options)

    def get_result_text(self) -> str:
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(MultSelectPageLocators.button, timeout=10000)
        if self.page.is_visible(MultSelectPageLocators.result_text):
            return (
                self.page.locator(MultSelectPageLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
