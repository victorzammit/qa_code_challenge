"""Pydantic models for field data validation/"""
from pydantic import BaseModel, UUID4, EmailStr, conint, field_validator
from datetime import datetime


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
    Age: conint(ge=18, le=120)


class CompanyField(BaseModel):
    """Pydantic model for Company field."""
    Company: str


class CountryField(BaseModel):
    """Pydantic model for Country field."""
    Country: str


class ProductField(BaseModel):
    """Pydantic model for Product field."""
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
    purchase_qty: float

class PurchaseAmountField(BaseModel):
    """Pydantic model for Purchase Amount field."""
    purchase_amount: float

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