class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)
        pos_speed = []

        for i in range(n):
            pos_speed.append([position[i],speed[i]])
        
        pos_speed.sort(key = lambda r: -r[0])

        time = []

        for i in range(n):
            time.append((target-pos_speed[i][0])/pos_speed[i][1])

        fleet=n
        for i in range(n-1):
            if time[i]>=time[i+1]:
                fleet-=1
                time[i+1]=time[i]
        return fleet

        