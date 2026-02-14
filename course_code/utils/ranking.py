import pandas as pd


def rank_tracks_by_metric(df: pd.DataFrame, metric: str = "rank") -> pd.DataFrame:
    """
    Sort tracks by a numeric metric (descending).
    """
    return df.sort_values(by=metric, ascending=False).reset_index(drop=True)
