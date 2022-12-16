class SearchStatusViewGenerator:
    
    def __init__(self, rate = 100):
        self.rate = rate
        self.iter = 0

    def write(self, obj, sameLine = True):
        if self.iter % self.rate == 0:
            if sameLine:
                print(obj, end = "\r")
            else:
                print(obj)