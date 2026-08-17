class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        
        if sum(gas)<sum(cost):
            return -1

        curr_cost=0
        start_i=0
        
        for i in range(n+1):
            curr_cost+=gas[i%n]-cost[i%n]
            if curr_cost<0:
                curr_cost=0
                start_i=(i+1)%n

        return start_i

        
        # if sum(diff)<0:
        #     return -1
        
        # def checkRun(i):
        #     res=0
        #     for j in range(n):
        #         res+=gas[i%n]
        #         res-=cost[i%n]
        #         if res<0:
        #             return False
        #         i+=1
        #     return True

        # for i in range(n):
        #     if diff[i]>=0 and checkRun(i):
        #         return i

        # return -1
                
        

