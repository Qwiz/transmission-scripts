import requests

class Pushover:
    '''
    Class for pushover notification system
    '''
    def __init__(self, user_token, api_token, title, message, device=None):
        self.user = user_token
        self.api = api_token
        self.device = device
        self.title = title
        self.message = message
        self.base_url = "https://api.pushover.net/1/"
        self.api_url = self.base_url + "messages.json"
        self.validate_url = self.base_url + "users/validate.json"

    def sendmessage(self):
        payload = {"user": self.user,"token": self.api}
        if self.device:
            payload["device"] = self.device
        request = requests.post(self.validate_url, data=payload)
        if request.ok:
            payload["title"] = self.title
            payload["message"] = self.message
            requests.post(self.api_url, data=payload)
