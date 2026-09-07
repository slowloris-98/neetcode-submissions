class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp,value))
        #print(self.time_map)

    def get(self, key: str, timestamp: int) -> str:
        #print(self.time_map)
        if key not in self.time_map:
            return ""
        key_list = self.time_map[key]
        l,r = 0, len(key_list)-1
        res=""
        while l<=r:
            mid = (l+r)//2
            if key_list[mid][0]<=timestamp:
                res = key_list[mid][1]
                l=mid+1
            else:
                r=mid-1
        return res
        
