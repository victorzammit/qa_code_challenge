# Betsson Code Challenge
## Introduction
This project contains all the code to check the consistency of the provided dataset.
Tests are categorized into two:
- **Table integrity tests**:
  - Test checking that all required columns are present
  - Test checking that no unexpected columns are present
  - Test checking that there are no duplicate rows.
- **Data field type tests**:
  - Data type testing
  - For PurchaseDate, checks that date is in the past-present
  - For Age, checks that age is greater than 18 (assumed legal age), to a maximum cutoff
  - For country, checks that country is valid.

## Requirements
- [python3.12.10](https://www.python.org/downloads/release/python-31210/)
- [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

## How to install poetry
```shell
curl -sSL https://install.python-poetry.org | python3.13
```

## Poetry virtual environment

If you want poetry to install the virtualenvs in the project run
```shell
poetry config virtualenvs.in-project true
```

Then, from the project folder, run the following command to create the virtualenv and resolve the
dependencies.
```shell
poetry install
```

## Run Tests
One can run the tests by:
```shell
poetry run python3 run_tests.py
```
Alternatively, one can run tests on any IDE by navigating to ```build/tests```, and running the tests
individually.