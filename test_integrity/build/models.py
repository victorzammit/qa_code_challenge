from pydantic import BaseModel, UUID4, EmailStr, conint, field_validator
from datetime import datetime

class CustomerIDField(BaseModel):
    CustomerID: UUID4

class NameField(BaseModel):
    Name: str

class EmailField(BaseModel):
    Email: EmailStr

class AgeField(BaseModel):
    Age: conint(ge=18, le=120)

class CompanyField(BaseModel):
    Company: str

class CountryField(BaseModel):
    Country: str

class ProductField(BaseModel):
    Product: str

class PurchaseDateField(BaseModel):
    PurchaseDate: datetime

    @field_validator("PurchaseDate")
    @classmethod
    def date_must_be_in_past(cls, value:datetime):
        if value > datetime.now():
            raise ValueError('Purchases cannot be in the future')
        return value


class PurchaseQtyField(BaseModel):
    purchase_qty: float

class PurchaseAmountField(BaseModel):
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
    pass