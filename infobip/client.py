import importlib.metadata
import sys
from os import getenv

from httpx import AsyncClient

from infobip.api.mms import MMSClient
from infobip.api.sms import SMSClient


class APIClient(AsyncClient):
    def __init__(self, base_url=None, api_key: str = None):
        if base_url is None:
            base_url = getenv("IB_BASE_URL")
        if api_key is None:
            api_key = getenv("IB_API_KEY")

        headers = {"Authorization": f"App {api_key}"}
        headers.update({"User-Agent": self.__get_user_agent()})

        super().__init__(base_url=base_url, headers=headers)

        self.SMS = SMSClient(self)
        self.MMS = MMSClient(self)

    def __get_user_agent(cls) -> str:
        return f"@infobip/python-sdk{cls.__get_package_version()} python/{sys.version.split(' ')[0]}"

    def __get_package_version(cls) -> str:
        sdk_version = ""
        if "infobip_channels" in sys.modules:
            try:
                sdk_version = "/" + importlib.metadata.distribution("infobip").version
            except importlib.metadata.PackageNotFoundError:
                # Ignore as package is not installed in development environment.
                pass

        return sdk_version
