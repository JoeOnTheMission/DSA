class UndergroundSystem:
    def __init__(self):
        self.check_in_map = {} #we store the start station and the time [start_station,start_time]
        self.check_out_map = {}# (start, end) -> [totalTime, count]
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_map[id] = (stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_map[id]
        route = (start_station, stationName)
        if route not in self.check_out_map:
            self.check_out_map[route] = [0,0]
        self.check_out_map[route][0] += (t - start_time)
        self.check_out_map[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.check_out_map[(startStation, endStation)]
        return total_time / count