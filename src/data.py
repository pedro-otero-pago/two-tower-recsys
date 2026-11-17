import pandas as pd

RAW = "data/raw/benchmark/5core/rating_only/Video_Games.csv"


def load_interactions(path=RAW):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df.timestamp, unit="ms")
    return df.sort_values("timestamp").reset_index(drop=True)


def temporal_split(df, val_start="2021-07-01", test_start="2022-01-01", test_end="2022-07-01"):
    train = df[df.date < val_start]
    val = df[(df.date >= val_start) & (df.date < test_start)]
    test = df[(df.date >= test_start) & (df.date < test_end)]
    return train, val, test


def warm_only(part, train):
    """Keep only rows whose user and item both appear in train."""
    known_users, known_items = set(train.user_id), set(train.parent_asin)
    mask = part.user_id.isin(known_users) & part.parent_asin.isin(known_items)
    return part[mask]