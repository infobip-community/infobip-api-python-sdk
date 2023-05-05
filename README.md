# Infobip API Python SDK

[![Version](https://img.shields.io/pypi/v/infobip-api-python-sdk)](https://pypi.org/project/infobip-api-python-sdk/)
![Python](https://img.shields.io/pypi/pyversions/infobip-api-python-sdk)
[![Workflow](https://img.shields.io/github/workflow/status/infobip-community/infobip-api-python-sdk/Python%20package)](https://github.com/infobip-community/infobip-api-python-sdk/actions/workflows/python-package.yml)
![Release](https://img.shields.io/github/release-date/infobip-community/infobip-api-python-sdk)
[![Licence](https://img.shields.io/github/license/infobip-community/infobip-api-python-sdk)](LICENSE)

Client SDK to use the Infobip API with Python.

This package enables you to use multiple Infobip communication channels, like SMS, MMS, WhatsApp, Email, etc.

---

## 📡 Supported APIs

The following communication channels are supported:

- [SMS + 2FA](https://www.infobip.com/docs/api#channels/sms)
- [Whatsapp](https://www.infobip.com/docs/api#channels/whatsapp)
- [Email](https://www.infobip.com/docs/api#channels/email)
- [WebRTC](https://www.infobip.com/docs/api#channels/webrtc/)
- [MMS](https://www.infobip.com/docs/api#channels/mms)
- [RCS](https://www.infobip.com/docs/api#channels/rcs)

The following platform management APIs are supported:
- [Entities](https://www.infobip.com/docs/api/platform/application-entity)

More APIs to be added in the near future.

## 🔐 Authentication

Currently, infobip-api-python-sdk only supports API Key authentication,
and the key needs to be passed during client creation.
This will most likely change with future versions,
once more authentication methods are included.

## 📦 Installation

To install infobip SDK you will need to run:

```bash
pip install infobip
```

Details of the package can be found
in the [PyPI page](https://pypi.org/project/infobip/).

## 🚀 Usage

### Code Example
To use the package you'll need an Infobip account.
If you don't already have one, you can create a free trial account
[here](https://www.infobip.com/signup).

In this example, we will show how to send an SMS message.
Other channels can be used in a similar way.
The first step is to import the Infobip API Client and needed models.
Then you can use a context manager to create the client, and use it to call the API.
After calling the endpoint, you can parse the response into a response body object.
This code needs that you previously set the environment variables `IB_BASE_URL` and  `IB_API_KEY`.

```python
import asyncio
from infobip.client import APIClient
from infobip.models.sms_advanced_textual_request import SendSMSRequestBody
from infobip.models.sms_textual_message import Message
from infobip.models.sms_destination import Destination
from infobip.models.sms_response import SendSMSResponseBody


async def main():
    async with APIClient() as client:
        # Create a request body object and validate its contents.
        request_body = SendSMSRequestBody(
            messages=[
                Message(
                    destinations=[
                        Destination(
                            to="555555555555",
                        ),
                    ],
                    text="Hello from Infobip Python SDK!",
                )
            ]
        )

        # Call the endpoint and await returned Coroutine
        response = await client.SMS.send(request_body)

        # (Optional) Parse and validate response.
        response_body = SendSMSResponseBody.from_json(response.text)

        # Do something with the response.
        print(response)
        print(response_body)


if __name__ == "__main__":
    asyncio.run(main())
```

### Samples

We are adding samples in the [samples](samples) folder, which you can use as a reference on how to use the SDK
with real payloads.

## 🗒️ Notes

For SDK versioning we use
[Semantic Versioning](https://semver.org) scheme.

Python 3.6 is the minimum supported version by this library.

## 🧡 Want to help and improve this open-source SDK?

Check out our [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md).

## ⚖️ License

This library is distributed under the MIT license found in the [License](LICENSE).
