from pydantic_factories import ModelFactory

from infobip_channels.mms.models import MMSMessageBody


class MMSMessageBodyFactory(ModelFactory):
    __model__ = MMSMessageBody
