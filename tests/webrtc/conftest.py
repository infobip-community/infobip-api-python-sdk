from pydantic_factories import ModelFactory

from infobip_channels.web_rtc.models.body.generate_token import GenerateTokenBody
from infobip_channels.web_rtc.models.body.save_application import SaveApplicationBody


class GenerateTokenFactory(ModelFactory):
    __model__ = GenerateTokenBody


class SaveApplicationFactory(ModelFactory):
    __model__ = SaveApplicationBody
