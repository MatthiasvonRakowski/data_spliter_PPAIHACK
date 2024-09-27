class train_test:
    def __init__(
            self,
            train_size: int,
            test_size: int,
            batch_size: int | float = 1.0, # If int, it will be the max number of data, if float, it will be the percent of the data
            filter:bool = True, # Filter will be applied on the id pic if they are reused
            valid_train: float = 0.5, # If True, it will create a validation set
            ):
        self.train_size = train_size
        self.test_size = test_size
        self.batch_size = batch_size
        self.filter = filter
        self.valid_train = valid_train

    def create_train_test_data(self):
        pass