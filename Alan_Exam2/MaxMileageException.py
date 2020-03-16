class MaxMileageException(ValueError):
    def __init__(self, miles):
        super().__init__()
        self.miles = miles
