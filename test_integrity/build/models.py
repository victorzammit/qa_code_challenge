"""Pydantic models for field data validation/"""
from typing import Annotated
from datetime import datetime

import pycountry

from thefuzz import process
from pydantic import BaseModel, UUID4, EmailStr, field_validator, Field


class CustomerIDField(BaseModel):
    """Pydantic model for Customer ID field."""
    CustomerID: UUID4


class NameField(BaseModel):
    """Pydantic model for Name field."""
    Name: str


class EmailField(BaseModel):
    """Pydantic model for Email field."""
    Email: EmailStr


class AgeField(BaseModel):
    """Pydantic model for age field."""
    # enforcing age range (minimum age 18, maximum 120)
    Age: Annotated[int, Field(strict=True, gt=0, le=130)]


class CompanyField(BaseModel):
    """Pydantic model for Company field."""
    Company: str


class CountryField(BaseModel):
    """Pydantic model for Country field."""
    Country: str

    @field_validator('Country')
    @staticmethod
    def must_be_valid_country(value: str) -> str:
        """Validates country against default list in pycountry."""
        # FIXME: ideally here, original source creation of data is using an enumerated list of accepted countries.
        #  This would allow the direct use of enum values, and bypass the fuzzy find implemented here.
        country_name_list = [country.name for country in pycountry.countries]
        match, score = process.extractOne(value.strip(), country_name_list)
        if score < 80:
            raise ValueError(f"'{value}' is not a valid country. Closest match: {match}")
        return value

class ProductField(BaseModel):
    """Pydantic model for Product field."""
    # FIXME: Product type should be an enumeration of available products to purchase.
    #  This would allow checking entries more rigorously.
    Product: str


class PurchaseDateField(BaseModel):
    """Pydantic model for Purchase Date field."""
    PurchaseDate: datetime

    @field_validator("PurchaseDate")
    @classmethod
    def date_must_be_in_past_or_present(cls, value:datetime):
        """checks that purchase dates are not future dates."""
        if value > datetime.now():
            raise ValueError('Purchases cannot be in the future')
        return value


class PurchaseQtyField(BaseModel):
    """Pydantic model for Purchase Quantity field."""
    purchase_qty: Annotated[float, Field(strict=True, gt=0)]

class PurchaseAmountField(BaseModel):
    """Pydantic model for Purchase Amount field."""
    purchase_amount: Annotated[float, Field(strict=True, gt=0)]

class CustomerPurchaseRecord(
    CustomerIDField,
    NameField,
    EmailField,
    AgeField,
    CompanyField,
    CountryField,
    ProductField,
    PurchaseDateField,
    PurchaseQtyField,
    PurchaseAmountField,
):
    """Pydantic model for combined Customer Purchase Record field."""
    pass