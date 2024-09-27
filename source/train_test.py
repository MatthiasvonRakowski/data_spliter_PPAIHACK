import os
from random import randint, shuffle

class TrainTest:
    def __init__(
            self,
            train_size: int,
            batch_size: int | float = 1.0, # If int, it will be the max number of data, if float, it will be the percent of the data
            filter:bool = True, # Filter will be applied on the id pic if they are reused
            valid_train: float = 0.5, # If True, it will create a validation train set
            valid_test: float = 0.5, # If True, it will create a validation test set
            pressition: int = 100 # The pressition of the data needed corelate a
            ):
        self.train_size = train_size
        self.batch_size = batch_size
        self.filter = filter
        self.pressition = pressition
        self.valid_train = valid_train * self.pressition
        self.valid_test = valid_test * self.pressition
        self.train_data = []
        self.test_data = []
        self.id_pic = []

    def get_folder(self, folder: str):
        for root, dirs, files in os.walk(folder):
            for dir in dirs:
                self.get_folder(os.path.join(root, dir))
            count_train = 0
            count_test = 0
            for file in files:
                if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg"):
                    if "id" in file.lower() or "passport" in file.lower():
                        self.id_pic.append(os.path.join(root, file))
                    else:
                        random_batch = randint(0, self.pressition)
                        random_wrong = randint(0, self.pressition)
                        if random_batch <= self.train_size:
                            if random_wrong <= self.valid_train:
                                self.train_data.append([os.path.join(root, file), "", 1, "", ""])
                            else:
                                self.train_data.append([os.path.join(root, file), "", 0, "", ""])
                            count_train += 1
                        else:
                            if random_wrong <= self.valid_test:
                                self.test_data.append([os.path.join(root, file), "", 1, "", ""])
                            else:
                                self.test_data.append([os.path.join(root, file), "", 0, "", ""])
                            count_test += 1
            for i in range(count_train):
                self.train_data[- (i + 1)][3] = self.id_pic[-1]
                self.train_data[- (i + 1)][4] = self.id_pic[-2]
            for i in range(count_test):
                self.test_data[- (i + 1)][3] = self.id_pic[-1]
                self.test_data[- (i + 1)][4] = self.id_pic[-2]

    def build_id_connection(self, element: list):
        for ele in element:
            if ele[2] == 1:
                ele[1] = ele[randint(3, 4)]
            else:
                fake_id = randint(0, len(self.id_pic) - 1)
                while self.id_pic[fake_id] == ele[3] or self.id_pic[fake_id] == ele[4]:
                    fake_id = randint(0, len(self.id_pic) - 1)
                ele[1] = self.id_pic[fake_id]
            ele.pop()
            ele.pop()

    def create_train_test_data(self):
        self.get_folder("assets")
        shuffle(self.train_data)
        shuffle(self.test_data)
        self.build_id_connection(self.test_data)
        self.build_id_connection(self.train_data)