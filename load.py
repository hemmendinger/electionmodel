import pyarrow
from pyarrow import parquet


def dataframe_from_parquet(filepath):
    table = parquet.read_table(filepath, use_pandas_metadata=True)
    return table.to_pandas()


