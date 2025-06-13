import pandas as pd

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

def test_required_columns_are_present(table: pd.DataFrame) -> None:
    """Test checking whether all expected columns are present in the table."""
    all_columns_present: bool = True
    print('\n')
    for column in REQUIRED_COLUMNS:
        if column not in table.columns:
            print(f"Column {column} in table? ❌")
            all_columns_present = False
        else:
            print(f"Column {column} in table? ✅")
    assert all_columns_present