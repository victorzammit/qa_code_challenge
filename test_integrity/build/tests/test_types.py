"""Tests for valid data type entries in each column."""
import pytest
import pandas as pd

from pydantic import ValidationError

from test_integrity.build.models import (
    CustomerIDField,
    NameField,
    AgeField,
    EmailField,
    CompanyField,
    CountryField,
    ProductField,
    PurchaseDateField,
    PurchaseAmountField,
    PurchaseQtyField
)


def test_customer_id_types_are_valid(dataset) -> None:
    failure_list = []
    for row, customer_id in enumerate(dataset.CustomerID):
        try:
            CustomerIDField(CustomerID=customer_id)
        except ValidationError:
            print(f"Invalid customer ID in row {row + 1}: {customer_id} ❌")
            failure_list.append(f"Row {row + 1} -> Customer ID: {customer_id}")

    assert len(failure_list) == 0


def test_name_types_are_valid(dataset) -> None:
    failure_list = []
    for row, name in enumerate(dataset.Name):
        try:
            NameField(Name=name)
        except ValidationError:
            print(f"Invalid name in row {row + 1}: {name} ❌")
            failure_list.append(f"Row {row + 1} -> Name: {name}")

    assert len(failure_list) == 0


def test_email_types_are_valid(dataset) -> None:
    failure_list = []
    for row, email in enumerate(dataset.Email):
        try:
            EmailField(Email=email)
        except ValidationError:
            print(f"Invalid email in row {row + 1}: {email} ❌")
            failure_list.append(f"Row {row + 1} -> Email: {email}")

    assert len(failure_list) == 0


def test_age_types_are_valid(dataset) -> None:
    failure_list = []
    for row, age in enumerate(dataset.Age):
        try:
            AgeField(Age=age)
        except ValidationError:
            print(f"Invalid age in row {row + 1}: {age} ❌")
            failure_list.append(f"Row {row + 1} -> Age: {age}")

    assert len(failure_list) == 0


def test_company_types_are_valid(dataset) -> None:
    failure_list = []
    for row, company in enumerate(dataset.Company):
        try:
            CompanyField(Company=company)
        except ValidationError:
            print(f"Invalid company in row {row + 1}: {company} ❌")
            failure_list.append(f"Row {row + 1} -> Company: {company}")

    assert len(failure_list) == 0

def test_country_types_are_valid(dataset) -> None:
    failure_list = []
    for row, country in enumerate(dataset.Country):
        try:
            CountryField(Country=country)
        except ValidationError:
            print(f"Invalid country in row {row + 1}: {country} ❌")
            failure_list.append(f"Row {row + 1} -> Country: {country}")

    assert len(failure_list) == 0


def test_product_types_are_valid(dataset) -> None:
    failure_list = []
    for row, product in enumerate(dataset.Product):
        try:
            ProductField(Product=product)
        except ValidationError:
            print(f"Invalid product in row {row + 1}: {product} ❌")
            failure_list.append(f"Row {row + 1} -> Product: {product}")

    assert len(failure_list) == 0


def test_purchase_date_types_are_valid(dataset) -> None:
    failure_list = []
    for row, purchase_date in enumerate(dataset.PurchaseDate):
        try:
            PurchaseDateField(PurchaseDate=purchase_date)
        except ValidationError:
            print(f"Invalid purchase_date in row {row + 1}: {purchase_date} ❌")
            failure_list.append(f"Row {row + 1} -> Email: {purchase_date}")

    assert len(failure_list) == 0


def test_purchase_amount_types_are_valid(dataset) -> None:
    failure_list = []
    for row, purchase_amount in enumerate(dataset.PurchaseAmount):
        try:
            PurchaseAmountField(purchase_amount=purchase_amount)
        except ValidationError:
            print(f"Invalid purchase amount in row {row + 1}: {purchase_amount} ❌")
            failure_list.append(f"Row {row + 1} -> Purchase amount: {purchase_amount}")

    assert len(failure_list) == 0


def test_purchase_qty_types_are_valid(dataset: pd.DataFrame) -> None:
    failure_list = []
    for row, purchase_qty in enumerate(dataset.PurchaseQuantity):
        try:
            PurchaseQtyField(purchase_qty=purchase_qty)
        except ValidationError:
            print(f"Invalid purchase quantity in row {row + 1}: {purchase_qty} ❌")
            failure_list.append(f"Row {row + 1} -> Email: {purchase_qty}")

    assert len(failure_list) == 0