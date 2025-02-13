import requests

from notifier.notifier_base import NotifierBase


class Telegram(NotifierBase):
    def __init__(self):
        self.bot_token = self.config["TELEGRAM"]["bot_token"]
        self.base_url = f"https://api.telegram.org/bot{self.bot_token}"

    def send_message(self, recipient, content):
        """Envia uma mensagem para o Telegram."""
        url = f"{self.base_url}/sendMessage"
        payload = {"chat_id": recipient, "text": content}
        response = requests.post(url, data=payload)
        return response.json()
