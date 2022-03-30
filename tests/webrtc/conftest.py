from pydantic_factories import ModelFactory

from infobip_channels.web_rtc.models.body.generate_token import GenerateToken


class GenerateTokenFactory(ModelFactory):
    __model__ = GenerateToken
