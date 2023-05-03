from os import getenv
from httpx import AsyncClient

from api.mms import MMSClient
from api.sms import SMSClient


class InfobipAPIClient(AsyncClient):
    def __init__(self, base_url=None, api_key: str = None):
        if base_url is None:
            base_url = getenv("IB_BASE_URL")
        if api_key is None:
            api_key = getenv("IB_API_KEY")

        headers = {"Authorization": f"App {api_key}"}
        headers.update({"User-Agent": "infobip-api-python-sdk/6.0.0"})

        super().__init__(base_url=base_url, headers=headers)

        self.SMS = SMSClient(self)
        self.MMS = MMSClient(self)
