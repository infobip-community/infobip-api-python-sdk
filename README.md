# Infobip API Python SDK

[![Version](https://img.shields.io/pypi/v/infobip-api-python-sdk)](https://pypi.org/project/infobip-api-python-sdk/)
![Python](https://img.shields.io/pypi/pyversions/infobip-api-python-sdk)
[![Workflow](https://img.shields.io/github/workflow/status/infobip-community/infobip-api-python-sdk/Python%20package)](https://github.com/infobip-community/infobip-api-python-sdk/actions/workflows/python-package.yml)
![Release](https://img.shields.io/github/release-date/infobip-community/infobip-api-python-sdk)
[![Licence](https://img.shields.io/github/license/infobip-community/infobip-api-python-sdk)](LICENSE)
![Lines](https://img.shields.io/tokei/lines/github/infobip-community/infobip-api-python-sdk)

Python client for Infobip's  API channels.

---

## 📡 Supported channels
- [SMS Reference](https://www.infobip.com/docs/api#channels/sms)
- [Whatsapp Reference](https://www.infobip.com/docs/api#channels/whatsapp)
- [Email Reference](https://www.infobip.com/docs/api#channels/email)
- [WebRTC Reference](https://www.infobip.com/docs/api#channels/webrtc/)
- [MMS Reference](https://www.infobip.com/docs/api#channels/mms)
- [RCS Reference](https://www.infobip.com/docs/api#channels/rcs)

More channels to be added in the near future.

## ℹ️ General Info

For `infobip-api-python-sdk` versioning we use
[Semantic Versioning](https://semver.org) scheme.

Python 3.6 is minimum supported version by this library.

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
[here](https://pypi.org/project/infobip-api-python-sdk/)

## 🚀 Usage

### Code Example
To use the package you'll need an Infobip account.
If you don't already have one, you can create a free trial account
[here](https://www.infobip.com/signup).

In this example we will show how to send WhatsApp text message.
Similar can be done for other channels.
First step is to import necessary channel, in this case WhatsApp channel.

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
## 🧪 Testing
To run tests position yourself in the project's root while your virtual environment
is active and run:
```bash
python -m pytest
```

## ✅ Enable pre-commit hooks
To enable pre-commit hooks run:
```bash
pip install -r requirements/dev.txt
```
You will need to install pre-commit hooks
Using homebrew:
```bash
brew install pre-commit
```
Using conda (via conda-forge):
```bash
conda install -c conda-forge pre-commit
```
To check installation run:
```bash
pre-commit --version
```
If installation was successful you will see version number.
You can find the Pre-commit configuration in `.pre-commit-config.yaml`.
Install the git hook scripts:
```bash
pre-commit install
```
Run against all files:
```bash
pre-commit run --all-files
```
If setup was successful pre-commit will run on every commit.
Every time you clone a project that uses pre-commit, running `pre-commit install`
should be the first thing you do.

## ⚖️ License

This library is distributed under the MIT license found in the [License](LICENSE).
