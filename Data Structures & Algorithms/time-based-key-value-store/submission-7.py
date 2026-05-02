class TimeMap:

    def __init__(self):
        self.time = {}
        self.prev = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time[(key,timestamp)] = value
        self.prev[key].append(timestamp)


    def get(self, key: str, timestamp: int) -> str:
        if (key,timestamp) not in self.time:
            if not self.prev[key]:
                return ""

            if not self.prev[key]:
                return ""
            i = len(self.prev[key]) - 1
            while i >= 0:
                if self.prev[key][i] <= timestamp:
                    return self.time[key,self.prev[key][i]]
                i -= 1
           
            return ""
   
        return  self.time[(key,timestamp)]
