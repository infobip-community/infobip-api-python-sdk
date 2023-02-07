from infobip_channels.core.models import MessageBodyBase
from infobip_channels.sms.models.core.tfa_message_template import TFAMessageTemplate


class CreateTFAMessageTemplateBody(MessageBodyBase, TFAMessageTemplate):
    pass
