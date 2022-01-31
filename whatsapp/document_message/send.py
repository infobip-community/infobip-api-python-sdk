import requests

from whatsapp.authentication.models import Authentication
from whatsapp.core.models import Response, RequestHeaders
from whatsapp.core.utils import construct_response_model
from whatsapp.document_message.models import MessageBody

ENDPOINT = "/whatsapp/1/message/document"


def send_message(auth: Authentication, message: MessageBody) -> Response:
    url = auth.base_url + ENDPOINT
    headers = RequestHeaders(authorization=auth.api_key)
    response = requests.post(
        url=url,
        json=message.dict(by_alias=True),
        headers=headers.dict(by_alias=True),
    )

    return construct_response_model(response)


