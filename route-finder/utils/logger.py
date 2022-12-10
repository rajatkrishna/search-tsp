class Logger:

    def __init__(self, enable : bool):
        self.enable = enable

    def log(self, *msgs):
        if self.enable:
            print(" ".join([str(msg) for msg in msgs]))