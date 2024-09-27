import zipfile
import os

class DownloadAssets:
    def folder(kaggle_folder: str):
        extract_to = "assets/" + kaggle_folder.split("/")[-1]

        os.system(f"kaggle datasets download -d {kaggle_folder} -p assets")
        os.makedirs(extract_to, exist_ok=True)
        zip_file_path = f"assets/{kaggle_folder.split('/')[-1]}.zip"
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        os.remove(zip_file_path)
