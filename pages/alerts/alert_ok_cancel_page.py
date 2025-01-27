from pages.base_page import BasePage
from playwright.sync_api import Dialog


class AlertOkCancelLocators:
    """Хранит локаторы для страницы с диалоговым окном."""

    # Кнопка вызова диалогового окна
    button = "a.a-button"

    # Результат
    result_text = "#result-text"


class AlertOkCancelPage(BasePage):
    """Представляет страницу с диалоговым окном."""

    def open(self):
        """Открывает страницу с диалоговым окном."""
        return super().open("https://www.qa-practice.com/elements/alert/confirm")

    def open_and_ok_or_cancel_alert(self, ok: bool) -> str:
        """Открывает диалоговое окно и принимает или отклоняет его в зависимости от параметра.

        Args:
            ok (bool): Если True, принимает диалоговое окно; если False, отклоняет.

        Returns:
            str: Текст сообщения из диалогового окна.
        """
        message = ""

        def save_alert_text_and_ok(dialog: Dialog):
            """Сохраняет текст сообщения из диалогового окна и принимает или отклоняет его.

            Args:
                dialog (Dialog): Объект диалогового окна.
            """
            nonlocal message, ok
            message = dialog.message
            if ok:
                dialog.accept()
            else:
                dialog.dismiss()

        self.page.on("dialog", lambda dialog: save_alert_text_and_ok(dialog))
        self.click(AlertOkCancelLocators.button)
        return message

    def get_result_text(self):
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(AlertOkCancelLocators.button)
        if self.page.is_visible(AlertOkCancelLocators.result_text, timeout=10000):
            return (
                self.page.locator(AlertOkCancelLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
