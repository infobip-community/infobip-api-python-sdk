# infobip-python-whatsapp-client
Python client for Infobip's Whatsapp API.

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
Every time you clone a project using pre-commit running `pre-commit install` should always be the first thing you do.
