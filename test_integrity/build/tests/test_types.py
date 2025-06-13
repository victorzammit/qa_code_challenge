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
    for customer_id in dataset.CustomerID:
        try:
            CustomerIDField(CustomerID=customer_id)
        except ValidationError:
            pytest.fail(f"Invalid UUID: {customer_id}")


def test_name_types_are_valid(dataset) -> None:
    for name in dataset.Name:
        try:
            NameField(Name=name)
        except ValidationError:
            pytest.fail(f"Invalid Name: {name}")


def test_email_types_are_valid(dataset) -> None:
    for email in dataset.Email:
        try:
            EmailField(Email=email)
        except ValidationError:
            pytest.fail(f"Invalid email: {email}")


def test_age_types_are_valid(dataset) -> None:
    for age in dataset.Age:
        try:
            AgeField(Age=age)
        except ValidationError:
            pytest.fail(f"Invalid age: {age}")


def test_company_types_are_valid(dataset) -> None:
    for company in dataset.Company:
        try:
            CompanyField(Company=company)
        except ValidationError:
            pytest.fail(f"Invalid company: {company}")


def test_country_types_are_valid(dataset) -> None:
    for country in dataset.Country:
        try:
            CountryField(Country=country)
        except ValidationError:
            pytest.fail(f"Invalid country: {country}")


def test_product_types_are_valid(dataset) -> None:
    for product in dataset.Product:
        try:
            ProductField(Product=product)
        except ValidationError:
            pytest.fail(f"Invalid product: {product}")


def test_purchase_date_types_are_valid(dataset) -> None:
    for purchase_date in dataset.PurchaseDate:
        try:
            PurchaseDateField(PurchaseDate=purchase_date)
        except ValidationError:
            pytest.fail(f"Invalid purchase date: {purchase_date}")


def test_purchase_amount_types_are_valid(dataset) -> None:
    for purchase_amount in dataset.PurchaseAmount:
        try:
            PurchaseAmountField(purchase_amount=purchase_amount)
        except ValidationError:
            pytest.fail(f"Invalid purchase amount: {purchase_amount}")


def test_purchase_qty_types_are_valid(dataset: pd.DataFrame) -> None:
    for purchase_qty in dataset.PurchaseQuantity:
        try:
            PurchaseQtyField(purchase_qty=purchase_qty)
        except ValidationError:
            pytest.fail(f"Invalid purchase quantity: {purchase_qty}")