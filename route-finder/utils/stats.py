import time

class Stats:

    def __init__(self):
        self.startTime = time.perf_counter()
        self.nodeCount = 0
        self.totalCost = 0

    def endTime(self):
          self.totalTime = time.perf_counter() - self.startTime
