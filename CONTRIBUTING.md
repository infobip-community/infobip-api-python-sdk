# Contributing to Infobip Community

✨✨ First off, thanks for taking the time to contribute! ✨✨

This project adheres to the Contributor Covenant [code of conduct](CODE_OF_CONDUCT.md). By participating,
you are expected to uphold this code. Please report unacceptable behavior to DevRel@infobip.com.

The following is a set of guidelines for contributing to Infobip's SDKs or any other projects,
which are hosted in the [Infobip Organisation](https://github.com/infobip-community)  on GitHub.
These are mostly guidelines, not rules. Use your best judgment,
and feel free to propose changes to this document in a pull request.

## 🚩 Issues
How to report a bug?

Bugs are tracked as [GitHub issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues). After you've determined which repository your bug is related to,
create an issue on that repository and provide the following information by filling in comment section.

Explain the problem and include additional details to help maintainers reproduce the problem:
* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible.
* **Provide specific examples to demonstrate the steps**.
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why.**
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.

## ℹ️ Asking for General Help

The [Infobip website](https://www.infobip.com/docs/api) has a list of resources for getting programming help and more.
For any question contributors are available at [DevRel@infobip.com](mailto:DevRel@infobip.com).
Please use the issue tracker for bugs only!

## ⬇️ Pull request

### 🍴 Step 1: Fork
Fork the project on GitHub and clone your fork locally.
Example for Python SDK repository:
```bash
git clone https://github.com/<your username>/infobip-api-python-sdk.git
cd infobip-api-python-sdk
git remote add upstream https://github.com/infobip-community/infobip-api-python-sdk.git
git fetch upstream
```
### 🛠️ Step 2: Build
Please run all tests that are in repository, all test should pass.
Please check do you need to activate some additional features that are repository or language specific.
For example in infobip-api-python-sdk, pre-commit hooks must be enabled. See Commit section below.

### 🌱 Step 3: Branch
To keep your development environment organized, create local branches to hold your work.
These should be branched directly off of the main branch.

```bash
git checkout -b my-branch -t upstream/main
```

### 💻 Step 4: Code
Please follow code structure and naming structure that is already in specific repositories.
Please be sure to run linters for specific repository from time to time on any code changes to ensure that they follow the project's code style.
For Python repository we mostly conform to [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/).
There are some deviations from PEP8.
Most important things to keep in mind are:
* Codebase has four-space indentation
* Codebase is using Pascal case for classes (ex. MessageBodyBase)
* Codebase is using snake case for methods (ex. send_sms_message)
* 88 character line limits rather than 79. (differ from PEP-8)

### ✅ Step 5: Commit

#### Enable pre-commit hooks (recommended)
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

#### Commit changes

It is recommended to keep your changes grouped logically within individual commits.
Many contributors find it easier to review changes that are split across multiple commits.
There is no limit to the number of commits in a pull request.

```bash
git add my/changed/files
git commit
```

Note that multiple commits get squashed when they are landed.
A good commit message should describe what changed and why.
Commit message should:

* Contain a short description of the change (preferably 50 characters or less, and no more than 72 characters)
* First letter should be capital and rest entirely in lowercase with the exception of proper nouns, acronyms,
and the words that refer to code, like function/variable names

#### ⚠️ Breaking Changes

When commit has the breaking change first line of commit text should be BREAKING CHANGE.

### 📌 Step 6: Rebase
Once you have committed your changes, it is a good idea to use git rebase (not git merge) to synchronize your work with the main repository.
```bash
git fetch upstream
git rebase upstream/main
```

### 🧪 Step 7: Tests
Bug fixes and features should always come with tests. Looking at other tests to see how they should be structured can also help.
Before submitting your changes in a pull request, always run the full test suite.
Make sure the linter does not report any issues and that all tests pass. Please do not submit patches that fail either check.

To run tests position yourself in the project's root while your virtual environment
is active and run:
```bash
python -m pytest
```

### 🚀 Step 8: Push
Once your commits are ready to go -- with passing tests and linting -- begin the process of opening a pull request by pushing your working branch to your fork on GitHub.
```bash
git push origin my-branch
```

### 📬 Step 9: Opening the Pull Request
From within GitHub, open new pull request. Add repository admins as reviewers.
Your PR may be delayed in being merged as maintainers seek more information or clarify ambiguities.

### 🤼 Step 10: Discuss and update
You will probably get feedback or requests for changes to your pull request.
This is a big part of the submission process so don't be discouraged!
Some contributors may sign off on the pull request right away.
Others may have detailed comments or feedback.
This is a necessary part of the process in order to evaluate whether the changes are correct and necessary.

To make changes to an existing pull request, make the changes to your local branch,
add a new commit with those changes, and push those to your fork. GitHub will automatically update the pull request.

```bash
git add my/changed/files
git commit
git push origin my-branch
```

Feel free to post a comment in the pull request to ping reviewers if you are awaiting an answer on something.

### 🌍 Step 11: Landing

In order to land, a pull request needs to be reviewed and approved by at least one repository Owner and pass CI.
After that, if there are no objections from other contributors, the pull request can be merged.

🎉🎊 Congratulations and thanks for your contribution! 🎊🎉

Every pull request is tested on the Continuous Integration (CI) system to confirm that it works.
Ideally, the pull request will pass ("be green") on all of CI's tests.
This means that all tests pass and there are no linting errors.
However, it is not uncommon for the CI infrastructure itself to fail on specific platforms or for so-called "flaky" tests to fail ("be red").
Each CI failure must be manually inspected to determine the cause.

## 📜 Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code.
Please report unacceptable behavior to [DevRel@infobip.com](mailto:DevRel@infobip.com).

## 📚 Further Reading

For more in-depth guides on developing SDKs, see
[Readme](README.md) and [Infobip's website](https://www.infobip.com/docs/api).
