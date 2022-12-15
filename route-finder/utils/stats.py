import time
from datetime import timedelta

class Stats:

    def __init__(self):
        self.startTime = time.perf_counter()
        self.nodeCount = 0
        self.totalCost = 0

    def endTime(self):
          self.totalTime = time.perf_counter() - self.startTime

    def toPrettyString(self):
        response = "Total time(HH:MM:SS)\tNodes expanded\tCost of route\n"
        response += str(timedelta(seconds=self.totalTime)) + "\t\t" + str(self.nodeCount) + "\t\t" + str(self.totalCost)
        return response