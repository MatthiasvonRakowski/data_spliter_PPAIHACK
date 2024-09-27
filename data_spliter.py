import os
from source.download_assets import DownloadAssets

def download_assets():
    assets = os.listdir("assets")
    folder1 =  "axondata/selfie-and-official-id-photo-dataset-18k-images"
    folder2 = "tapakah68/selfies-id-images-dataset"
    if not assets.__contains__(folder1.split("/")[-1]):
        DownloadAssets.folder(folder1)
    if not assets.__contains__(folder2.split("/")[-1]):
        DownloadAssets.folder(folder2)


def main():
    download_assets()



if __name__ == '__main__':
    main()
