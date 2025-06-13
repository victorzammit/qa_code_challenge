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

def test_no_unexpected_columns_are_present(required_columns: tuple[str, ...],
                                           dataset: pd.DataFrame) -> None:
    """Test checking whether there are no unexpected columns in the table."""
    assert not set(dataset.columns) - set(required_columns)

def test_no_duplicate_rows_are_present(dataset: pd.DataFrame) -> None:
    """Test checking that there are no identical rows in the table."""
    assert not dataset.duplicated().any()
