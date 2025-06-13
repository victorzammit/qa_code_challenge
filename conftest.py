import pandas as pd
from _pytest.fixtures import fixture


@fixture
def table():
    return pd.read_csv('dataset/test_dataset.csv')

