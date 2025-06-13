from datetime import datetime

import pandas as pd
from pydantic import BaseModel, EmailStr, conint, ValidationError

REQUIRED_COLUMNS = (
    "CustomerID",
    "Name",
    "Email",
    "Age",
    "Company",
    "Country",
    "Product",
    "PurchaseDate",
    "PurchaseQuantity",
    "PurchaseAmount"
)

class CustomerPurchaseRecord(BaseModel):
    CustomerID: int
    Name: str
    Email: EmailStr
    Age: conint(ge=18, le=120)
    Company: str
    Country: str
    Product: str
    PurchaseDate: datetime
    PurchaseQuantity: float
    PurchaseAmount: float


def test_required_columns_are_present(dataset: pd.DataFrame) -> None:
    """Test checking whether all expected columns are present in the table."""
    all_columns_present: bool = True
    print('\n')
    for column in REQUIRED_COLUMNS:
        if column not in dataset.columns:
            print(f"Column {column} in table? ❌")
            all_columns_present = False
        else:
            print(f"Column {column} in table? ✅")
    assert all_columns_present