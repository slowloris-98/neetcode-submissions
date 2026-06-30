class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # # freq count sorting -? nlogn
        # counter = Counter(nums)
        # freq_count=defaultdict(list)
        # for num, count in counter.items():
        #     freq_count[count].append(num)
        
        # sort_list = sorted(freq_count.items(), reverse=True)
        # res=[]
        # for count,num_list in sort_list:
        #     for num in num_list:
        #         if len(res)<k:
        #             res.append(num)
        # return res

        # # freq_count maxheap
        # counter = Counter(nums)
        # freq_count = [[] for i in range(len(counter))]
        # i=0
        # for num, count in counter.items():
        #     freq_count[i] = (-count,num)
        #     i+=1
        
        # heapq.heapify(freq_count)
        # res=[]
        # for i in range(k):
        #     res.append(heapq.heappop(freq_count)[1])
        # return res

        # bucket sort
        counter = Counter(nums)

        bucket=[[] for i in range(len(nums)+1)]
        for num, count in counter.items():
            bucket[count].append(num)
        
        print(bucket)

        res=[]
        for i in range(len(bucket)-1,-1,-1):
            for item in bucket[i]:
                res.append(item)
                k-=1
                if k==0:
                    return res
        return res


        









    
