"""Tests for whole-table structure integrity checking."""
import pandas as pd

def test_required_columns_are_present(required_columns: tuple[str, ...], dataset: pd.DataFrame) -> None:
    """Test checking whether all expected columns are present in the table."""
    all_columns_present: bool = True
    print('\n')
    for column in required_columns:
        if column not in dataset.columns:
            print(f"Column {column} in table? ❌")
            all_columns_present = False
        else:
            print(f"Column {column} in table? ✅")
    assert all_columns_present