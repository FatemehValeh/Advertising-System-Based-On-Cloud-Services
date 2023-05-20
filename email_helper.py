import requests


class Email:
    def __init__(self):
        self.domain_name = "sandboxa0c1c665256c43cf8f2f31ecd0fc5a5f.mailgun.org"
        self.api_key = "a6c6082b7442c2063f3507a2c9033afe-2de3d545-85b40163"

    def send_email(self, email, subject, text):
        return requests.post(
            f"https://api.mailgun.net/v3/{self.domain_name}/messages",
            auth=("api", self.api_key),
            data={"from": f"<mailgun@{self.domain_name}>",
                  "to": [email],
                  "subject": subject,
                  "text": text})
