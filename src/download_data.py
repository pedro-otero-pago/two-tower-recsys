from pathlib import Path
from huggingface_hub import hf_hub_download

Path("data/raw").mkdir(parents=True, exist_ok=True)
path = hf_hub_download(
    repo_id="McAuley-Lab/Amazon-Reviews-2023",
    repo_type="dataset",
    filename="benchmark/5core/rating_only/Video_Games.csv",
    local_dir="data/raw",
)
print(path)