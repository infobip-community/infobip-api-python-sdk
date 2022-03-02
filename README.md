# infobip-api-python-sdk
Python client for Infobip's  API channels.

#### Table of contents:

- [General Info](#general-info)
- [License](#license)
- [Installation](#installation)
- [Code example](#code-example)
- [Testing](#testing)
- [Enable pre-commit hooks](#enable-pre-commit-hooks)
- [Generating distribution package](#generating-distribution-package)
- [Uploading distribution package on TestPyPI](#uploading-distribution-package-on-testpypi-for-testing-purposes)
- [Installing your newly uploaded package](#installing-your-newly-uploaded-package)


## General Info

For `infobip-api-python-sdk` versioning we use [Semantic Versioning](https://semver.org) scheme.

Python 3.6 is minimum supported version by this library.

## License

Published under [MIT License](LICENSE).

## Installation

Install the library by using the following command:
```
pip install infobip-api-python-sdk
```

## Code Example
To use the package you'll need an Infobip account.
If you don't already have one, you can create a free trial account [here](https://www.infobip.com/signup).

In this example we will show how to send WhatsApp text message.
First step is to import necessary channel, in this case WhatsApp channel.

```
from infobip_channels import WhatsAppChannel
```

Now you can create instance of `WhatsAppChannel` with your `base_url` and `api_key`.

```
c = WhatsAppChannel.from_auth_params({
    "base_url": "<your_base_url>",
    "api_key": "<your_api_key>"
})
```
After that you can access all the methods from `WhatsAppChannel`.
To send text message you can use `send_text_message` method and add correct payload:
```
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
## Testing
To run tests position yourself in the project's root while your virtual environment
is active and run:
```
python -m pytest
```

## Enable pre-commit hooks
To enable pre-commit hooks run:
```
pip install -r requirements/dev.txt
```
You will need to install pre-commit hooks
Using homebrew:
```
brew install pre-commit
```
Using conda (via conda-forge):
```
conda install -c conda-forge pre-commit
```
To check installation run:
```
pre-commit --version
```
If installation was successful you will see version number.
You can find the Pre-commit configuration in `.pre-commit-config.yaml`.
Install the git hook scripts:
```
pre-commit install
```
Run against all files:
```
pre-commit run --all-files
```
If setup was successful pre-commit will run on every commit.
Every time you clone a project that uses pre-commit, running `pre-commit install`
should be the first thing you do.


## Generating distribution package
Make sure you have the latest version of PyPA's
[build](https://packaging.python.org/en/latest/key_projects/#build) installed:
```
python -m pip install --upgrade build
```
After installation check `setup.cfg` file for metadata.
Name and version are used for file generation.
Make sure that you appropriately change version before build.
Update the `version` in the  `setup.cfg` file to the desired one.

Now run this command from the same directory where pyproject.toml is located:
```
python -m build
```

This command should generate two files in the `dist` directory:
```
dist/
  infobip_channels-x.y.z-py3-none-any.whl
  infobip-channels-x.y.z.tar.gz
```


## Uploading distribution package on TestPyPI (for testing purposes)
First thing to do is create an account on TestPyPI and acquire an API token.
To upload the distribution package, you can use
[twine](https://packaging.python.org/en/latest/key_projects/#twine):
```
python -m pip install --upgrade twine
```

Once installed, run Twine to upload all the archives under dist:
```
python -m twine upload --repository testpypi dist/*
```

You will be prompted for a username and password. For the username, use *\_\_token\_\_*.
For the password, use the token value, including the pypi- prefix.


## Installing your newly uploaded package
To test the newly uploaded package, create a virtual environment and download the
package:
```
pip install --extra-index-url https://test.pypi.org/simple/ infobip-channels==x.y.z
```

After that, create a test script or import the library in a shell and try it out.
