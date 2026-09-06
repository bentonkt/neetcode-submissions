class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)
        self.values = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:

        times = self.times[key]
        if not times: 
            return ""

        l, r = 0, len(times) - 1

        while l < r: 
            # print(l)
            # print(r)
            # print("___")
            mid = (l+r)// 2

            if times[mid] == timestamp: 
                return self.values[(key, timestamp)]

            if times[mid] > timestamp: 
                r= mid-1
            else:
                l = mid + 1

        if times[l] == timestamp: 
            return self.values[(key, timestamp)]
        if times[l] < timestamp: 
            return self.values[(key, times[l])]
        return self.values[(key, times[l-1])] if l > 0 else ""
        
