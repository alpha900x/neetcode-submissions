class TimeMap:

    def __init__(self):
        self.hp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hp:
            self.hp[key].append([value,timestamp])
        else:
            self.hp[key] = [[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hp:
            return ""
        else:
            lv = self.hp[key]
            v=["",-1]
            l = 0
            r = len(lv)-1
            while l<=r:
                m=(l+r)//2
                if lv[m][1]<= timestamp and lv[m][1]>v[1]:
                    v = lv[m]
                    l = m+1
                else:
                    r = m-1
            return v[0]
            
