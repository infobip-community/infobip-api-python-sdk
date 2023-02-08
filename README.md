# Infobip API Python SDK

[![Version](https://img.shields.io/pypi/v/infobip-api-python-sdk)](https://pypi.org/project/infobip-api-python-sdk/)
![Python](https://img.shields.io/pypi/pyversions/infobip-api-python-sdk)
[![Workflow](https://img.shields.io/github/workflow/status/infobip-community/infobip-api-python-sdk/Python%20package)](https://github.com/infobip-community/infobip-api-python-sdk/actions/workflows/python-package.yml)
![Release](https://img.shields.io/github/release-date/infobip-community/infobip-api-python-sdk)
[![Licence](https://img.shields.io/github/license/infobip-community/infobip-api-python-sdk)](LICENSE)
![Lines](https://img.shields.io/tokei/lines/github/infobip-community/infobip-api-python-sdk)

Client SDK to use the Infobip API with Python.

This package enables you to use multiple Infobip communication channels, like SMS, MMS, WhatsApp, Email, etc.

---

## 📡 Supported channels

- [SMS + 2FA Reference](https://www.infobip.com/docs/api#channels/sms)
- [Whatsapp Reference](https://www.infobip.com/docs/api#channels/whatsapp)
- [Email Reference](https://www.infobip.com/docs/api#channels/email)
- [WebRTC Reference](https://www.infobip.com/docs/api#channels/webrtc/)
- [MMS Reference](https://www.infobip.com/docs/api#channels/mms)
- [RCS Reference](https://www.infobip.com/docs/api#channels/rcs)

More channels to be added in the near future.

## 🔐 Authentication

Currently, infobip-api-python-sdk only supports API Key authentication,
and the key needs to be passed during client creation.
This will most likely change with future versions,
once more authentication methods are included.

## 📦 Installation

To install infobip SDK you will need to run:

```bash
pip install infobip-api-python-sdk
```

Details of the package can be found
in the [PyPI page](https://pypi.org/project/infobip-api-python-sdk/).

## 🚀 Usage

### Code Example
To use the package you'll need an Infobip account.
If you don't already have one, you can create a free trial account
[here](https://www.infobip.com/signup).

In this example, we will show how to send a WhatsApp text message.
Other channels can be used in a similar way.
The first step is to import the necessary channel, in this case WhatsApp channel.

```python
from infobip_channels.whatsapp.channel import WhatsAppChannel
```

Now you can create instance of `WhatsAppChannel` with your `base_url` and `api_key`.

```python
c = WhatsAppChannel.from_auth_params({
    "base_url": "<your_base_url>",
    "api_key": "<your_api_key>"
})
```

Alternatively, you can create the instance from the environment, having the `IB_BASE_URL` and `IB_API_KEY` variables
set, like this:

```python
c = WhatsAppChannel.from_env()
```

After that you can access all the methods from `WhatsAppChannel`.
To send text message you can use `send_text_message` method and add correct payload:
```python
response = c.send_text_message(
    {
      "from": "<WhatsApp sender number from your Infobib account>",
      "to": "<Number that will receive WhatsApp message>",
      "messageId": "a28dd97c-1ffb-4fcf-99f1-0b557ed381da",
      "content": {
        "text": "Some text"
      },
      "callbackData": "Callback data",
      "notifyUrl": "https://www.example.com/whatsapp"
    }
)
```

### Samples

We are adding samples in the [samples](samples) folder, which you can use as a reference on how to use the SDK
with real payloads.

## 🗒️ Notes

For `infobip-api-python-sdk` versioning we use
[Semantic Versioning](https://semver.org) scheme.

Python 3.6 is the minimum supported version by this library.

## 🧡 Want to help and improve this open-source SDK?

Check out our [contributing guide](CONTRIBUTING.md) and [code of conduct](CODE_OF_CONDUCT.md).

## ⚖️ License

This library is distributed under the MIT license found in the [License](LICENSE).
