from google.cloud import storage
from typing import List

class GCSStorageService:
    def __init__(self, bucket_name: str):
        self.client = storage.Client()
        self.bucket = self.client.bucket(bucket_name)

    
    def list_files(self, game_id: str = "" ) -> List[str]:
        try:
            full_prefix = f"{game_id}/"
            blobs_iter = self.bucket.list_blobs(prefix=full_prefix)
            return [
                b.name.replace(f"{game_id}/", "", 1)
                for b in blobs_iter
                if not b.name.endswith('/')
            ]
        except Exception as e:
            raise RuntimeError(e)

    def read_file(self, file_path: str) -> str:
        try:
            print("filename from read file", file_path);
            blob = self.bucket.blob(file_path)
            return blob.download_as_text()
        except Exception as e:
            raise RuntimeError(e)
    def upload_file(self, file_path: str, file_content: str) -> None:
        try:
            blob = self.bucket.blob(file_path)
            blob.upload_from_string(file_content)
        except Exception as e:
            raise RuntimeError(e)
    def update_file(self, file_path: str, content: str) -> None:
        try:
            blob = self.bucket.blob(file_path)
            blob.upload_from_string(content, content_type="text/plain")
        except Exception as e:
            raise RuntimeError(e)
    def delete_file(self, file_path: str) -> None:
        try:
            blob = self.bucket.blob(file_path)
            blob.delete()
        except Exception as e:
            raise RuntimeError(e)
