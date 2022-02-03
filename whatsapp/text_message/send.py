import requests
from models.core import Authentication, RequestHeaders, Response
from models.text_message import TextMessageBody

from whatsapp.core.utils import construct_response_model

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
