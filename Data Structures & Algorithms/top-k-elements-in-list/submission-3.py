class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        # counter -> num: count
        # count: num
        # sort 
        # return val of top k

        counter = Counter(nums)
        freq_count=defaultdict(list)
        for num, count in counter.items():
            freq_count[count].append(num)
        #print(sorted(counter.items()))
        sort_list = sorted(freq_count.items(), reverse=True)
        #print(sort_list)
        res=[]
        for count,num_list in sort_list:
            for num in num_list:
                if len(res)<k:
                    res.append(num)
        

        return res



    
