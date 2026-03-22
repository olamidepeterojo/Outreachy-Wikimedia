# Outreachy-Wikimedia
## This repo is the second task for T418284

# URL Status Code Checker

This script reads a list of URLs from a CSV file and prints their HTTP status codes.

## Output format

`(STATUS_CODE) URL`

Example:
`(200) https://example.com`

## How to Setup

Clone the repository using `git`

```
git clone https://github.com/olamidepeterojo/Outreachy-Wikimedia.git
```

Go to the root repository
```
cd Outreachy-Wikimedia
```

It's recommended developers make a virtual environment to install all required dependencies.

To create a virtual environment in the root repository, run the command below:

```
python -m venv venv
```

Activate your virtual environment in order for python to use it to manage dependencies.

```
source venv/Scripts/activate
```

Or, check the table titled "Command to activate virtual environment" [here](https://docs.python.org/3/library/venv.html#how-venvs-work) to find what works for your shell.

## How to run

```
python status_code.py
```
