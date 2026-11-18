# two-tower-recsys
Two-tower recommender with retrieval and reranking in PyTorch, evaluated with a temporal split on Amazon Reviews 2023.

## Project structure

- `data/` — not in the repository. Created by `download_data.py`; it
  holds the Amazon Reviews 2023 (McAuley Lab) Video Games interactions.
- `src/download_data.py` — downloads the 5-core interactions file
  (user, item, rating, timestamp) from the Hugging Face dataset into
  `data/raw/`.
- `src/data.py` — loads and splits the interactions.
  - `load_interactions` converts the millisecond timestamps to dates
    and sorts the rows by time.
  - `temporal_split` splits by date into train (before July 2021),
    validation (July to December 2021) and test (January to June
    2022).
  - `warm_only` keeps the interactions whose user and item both appear
    in the training data.
