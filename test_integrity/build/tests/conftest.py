import pandas as pd
from pytest import fixture


@fixture(scope="session")
def dataset() -> pd.DataFrame:
    return pd.read_csv('../../../test_dataset.csv')

