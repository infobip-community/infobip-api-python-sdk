# infobip-python-whatsapp-client
Python client for Infobip's channels API.

## Testing
To run tests position yourself in the project's root while your virual environment
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
Pre-commit configuration you can find in `.pre-commit-config.yaml`.
Install the git hook scripts:
```
pre-commit install
```
Run against all files:
```
pre-commit run --all-files
```
If setup was successful pre-commit will run will now run on every commit.
Every time you clone a project using pre-commit running `pre-commit install`
should always be the first thing you do.


## Generating distribution package
Make sure you have the latest version of PyPA's
[build](https://packaging.python.org/en/latest/key_projects/#build) installed:
```
python -m pip install --upgrade build
```

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
To test the newly uploaded package, create a virtual environment and inside it run:
```
pip install -i https://test.pypi.org/simple/ infobip-channels==x.y.z
```

After that, create a test script or import the library in a shell and try it out.
