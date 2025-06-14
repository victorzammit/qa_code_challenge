import pytest
from pydantic import ValidationError, EmailStr

from build.data_models.models import (
    NameField,
    AgeField,
    EmailField,
    PurchaseQtyField
)

@pytest.mark.parametrize("invalid_email", ["not-email", "email@", "@email.com"])
def test_invalid_emails(invalid_email: EmailStr):
    with pytest.raises(ValidationError):
        EmailField(Email=invalid_email)

@pytest.mark.parametrize("invalid_age", ["twenty", -4, 0, 10, 140])
def test_invalid_email(invalid_age: int):
    with pytest.raises(ValidationError):
        AgeField(Age=invalid_age)

@pytest.mark.parametrize("invalid_purchase_qty", ["three", 0, -200, True])
def test_invalid_purchase_qty(invalid_purchase_qty: float):
    with pytest.raises(ValidationError):
        PurchaseQtyField(purchase_qty=invalid_purchase_qty)

@pytest.mark.parametrize("invalid_name", [0, True, 20.54, "", "     "])
def test_invalid_name(invalid_name: str):
    with pytest.raises(ValidationError):
        NameField(Name=invalid_name)

