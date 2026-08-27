class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count=[0]*3
        for num in nums:
            count[num]+=1
        k=0
        for i in range(3):
            while count[i]:
                nums[k]=i
                count[i]-=1
                k+=1
        return nums



        # count_nums = Counter(nums)
        # j=0


        # for i in range(count_nums.get(0,0)):
        #     nums[j]=0
        #     j+=1
        
        # for i in range(count_nums.get(1,0)):
        #     nums[j]=1
        #     j+=1

        # for i in range(count_nums.get(2,0)):
        #     nums[j]=2
        #     j+=1
        
        # print(nums)
        # return nums

            
        

        
        