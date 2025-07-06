from huggingface_hub import hf_hub_download

# 저장할 경로
save_dir = "data/raw"

# 다운로드 파일 목록
files = ["client_split.tar.gz", "detail.tar.gz", "targets.tar.gz"]

for fname in files:
    hf_hub_download(
        repo_id="ai-lab/MBD",
        filename=fname,
        repo_type="dataset",
        local_dir=save_dir,
        local_dir_use_symlinks=False  # 실파일로 복사
    )