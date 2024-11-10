class UndergroundSystem:
    def __init__(self):
        self.queries = {} # (a,b) -> (total, count)
        self.seen = {} # id -> (time, start)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.seen[id] = (t, stationName)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startTime, startStation = self.seen[id]
        key = (startStation, stationName)
        if key not in self.queries:
            self.queries[key] = [0, 0]
        
        self.queries[key][0] += t-startTime
        self.queries[key][1] += 1

        del self.seen[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.queries[(startStation, endStation)]
        return total/count
