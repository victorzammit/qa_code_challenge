"""conftest.py"""
import os
import pandas as pd
from pytest import fixture


@fixture(scope="session")
def dataset() -> pd.DataFrame:
    path = os.path.join(os.path.dirname(__file__), "..", "..", "raw_data", "test_dataset.csv")
    return pd.read_csv(path)

@fixture(scope="session")
def required_columns() -> tuple[str, ...]:
    return (
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