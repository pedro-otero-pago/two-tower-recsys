from huggingface_hub import list_repo_files

files = list_repo_files("McAuley-Lab/Amazon-Reviews-2023", repo_type="dataset")
print([f for f in files if "Video_Games" in f])