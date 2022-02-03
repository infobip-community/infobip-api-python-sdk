import requests
from core.models import Authentication

from whatsapp.core.models import RequestHeaders, Response
from whatsapp.core.utils import construct_response_model
from whatsapp.text_message.models import TextMessageBody

ENDPOINT = "/whatsapp/1/message/text"


def send_message(auth: Authentication, message: TextMessageBody) -> Response:
    url = auth.base_url + ENDPOINT
    headers = RequestHeaders(authorization=auth.api_key)
    response = requests.post(
        url=url,
        json=message.dict(by_alias=True),
        headers=headers.dict(by_alias=True),
    )

    return construct_response_model(response)
