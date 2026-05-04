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
            left = 0
            m = float("inf")
            right = len(self.prev[key]) - 1
            while left <= right:
                middle = (left + right) // 2
                if self.prev[key][middle] <= timestamp:
                    m = self.prev[key][middle]
                    left = middle + 1
                else:
                    right = middle - 1  
            if m == float("inf"):
                return ""

            return self.time[(key,m)]
   
        return  self.time[(key,timestamp)]

# Solution in a binary search : set => time :o(1) ; get => time: o(log n) ; space:o(n)
