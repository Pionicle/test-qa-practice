from pages.base_page import BasePage
from playwright.sync_api import Dialog


class AlertOkLocators:
    """Хранит локаторы для страницы с диалоговым окном."""

    # Кнопка вызова диалогового окна
    button = "a.a-button"

    # Кнопка на домашнюю страницу
    homepage_link = "a[href='/']"


class AlertOkPage(BasePage):
    """Представляет страницу с диалоговым окном."""

    def open(self):
        """Открывает страницу с диалоговым окном."""
        return super().open("https://www.qa-practice.com/elements/alert/alert")

    def open_and_ok_alert(self) -> str:
        """Открывает диалоговое окно и принимает его, сохраняя текст сообщения.

        Returns:
            str: Текст сообщения из диалогового окна.
        """
        message = ""

        def save_alert_text_and_ok(dialog: Dialog):
            """Сохраняет текст сообщения из диалогового окна и принимает его.

            Args:
                dialog (Dialog): Объект диалогового окна.
            """
            nonlocal message
            message = dialog.message
            dialog.accept()

        self.page.on("dialog", lambda dialog: save_alert_text_and_ok(dialog))
        self.click(AlertOkLocators.button)
        return message

    def go_to_homepage(self):
        """Переходит на домашнюю страницу."""
        self.click(AlertOkLocators.homepage_link)
