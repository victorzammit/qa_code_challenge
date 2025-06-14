import pytest
from pydantic import ValidationError, EmailStr

from build.data_models.models import (
    NameField,
    AgeField,
    EmailField,
    PurchaseQtyField
)

@pytest.mark.parametrize("invalid_email", ["not-email", "email@", "@email.com"])
def test_invalid_email(invalid_email: EmailStr) -> None:
    with pytest.raises(ValidationError):
        EmailField(Email=invalid_email)


@pytest.mark.parametrize("invalid_age", ["twenty", -4, 0, 10, 140, 34.5])
def test_invalid_age(invalid_age: int) -> None:
    with pytest.raises(ValidationError):
        AgeField(Age=invalid_age)


@pytest.mark.parametrize("valid_age", [19, 50, 96, 110])
def test_valid_age(valid_age: int) -> None:
        age_field = AgeField(Age=valid_age)
        assert age_field.Age == valid_age


@pytest.mark.parametrize("invalid_purchase_qty", ["three", 0, -200, True])
def test_invalid_purchase_qty(invalid_purchase_qty: float) -> None:
    with pytest.raises(ValidationError):
        PurchaseQtyField(purchase_qty=invalid_purchase_qty)


@pytest.mark.parametrize("invalid_name", [0, True, 20.54, "", "     "])
def test_invalid_name(invalid_name: str) -> None:
    with pytest.raises(ValidationError):
        NameField(Name=invalid_name)

# TODO: Unit tests for the remaining field models are to be added here,
#  including cases for valid and invalid entries.