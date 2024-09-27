import os
from source.download_assets import DownloadAssets
from source.train_test import TrainTest
import csv

def download_assets():
    assets = os.listdir("assets")
    folder1 =  "axondata/selfie-and-official-id-photo-dataset-18k-images"
    folder2 = "tapakah68/selfies-id-images-dataset"
    if not assets.__contains__(folder1.split("/")[-1]):
        DownloadAssets.folder(folder1)
    if not assets.__contains__(folder2.split("/")[-1]):
        DownloadAssets.folder(folder2)

def create_csv(train_test: TrainTest):
    with open("train_data.csv", mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["file", "id", "result"])
        for data in train_test.train_data:
            writer.writerow(data)
    with open("test_data.csv", mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(["file", "id", "result"])
        for data in train_test.test_data:
            writer.writerow(data)


def main():
    download_assets()
    train_test = TrainTest(90)
    train_test.create_train_test_data()
    create_csv(train_test)


if __name__ == '__main__':
    main()
