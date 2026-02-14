import pandas as pd
import numpy as np


def compute_basic_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute basic descriptive statistics for numeric columns.
    """
    numeric_cols = df.select_dtypes(include=np.number)
    stats = numeric_cols.agg(["mean", "std", "min", "max"])
    return stats
