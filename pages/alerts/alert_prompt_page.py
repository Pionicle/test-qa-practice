from pages.base_page import BasePage
from playwright.sync_api import Dialog


class AlertPromptLocators:
    """Хранит локаторы для страницы с диалоговым окном."""

    # Кнопка вызова диалогового окна
    button = "a.a-button"

    # Результат
    result_text = "#result-text"


class AlertPromptPage(BasePage):
    """Представляет страницу с диалоговым окном."""

    def open(self):
        """Открывает страницу с диалоговым окном."""
        return super().open("https://www.qa-practice.com/elements/alert/prompt")

    def open_and_promt_alert(self, ok: bool, promt_text: str) -> str:
        """Открывает диалоговое окно с текстом и принимает или отклоняет его, передавая текст в случае принятия.

        Args:
            ok (bool): Если True, принимает диалоговое окно с текстом; если False, отклоняет.
            prompt_text (str): Текст, который будет передан в диалоговое окно при его принятии.

        Returns:
            str: Текст сообщения из диалогового окна.
        """
        message = ""

        def save_alert_text_and_ok(dialog: Dialog):
            """Сохраняет текст сообщения из диалогового окна и принимает или отклоняет его.

            Args:
                dialog (Dialog): Объект диалогового окна.
            """
            nonlocal message, ok, promt_text
            message = dialog.message
            if ok:
                dialog.accept(promt_text)
            else:
                dialog.dismiss()

        self.page.on("dialog", lambda dialog: save_alert_text_and_ok(dialog))
        self.click(AlertPromptLocators.button)
        return message

    def get_result_text(self):
        """Получает текст результата.

        Returns:
            str: Текст результата, если он видим; иначе пустая строка.
        """
        self.page.wait_for_selector(AlertPromptLocators.button)
        if self.page.is_visible(AlertPromptLocators.result_text, timeout=10000):
            return (
                self.page.locator(AlertPromptLocators.result_text)
                .text_content()
                .strip()
            )
        return ""
