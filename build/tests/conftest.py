import pandas as pd
from pytest import fixture


@fixture(scope="session")
def dataset() -> pd.DataFrame:
    return pd.read_csv('../../raw_data/test_dataset.csv')

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