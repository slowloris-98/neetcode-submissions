class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2 pointer
        i,j = 0,0
        #count=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i




        
        # brute force
        # temp=[]
        # count=0
        # for n in nums:
        #     if n!=val:
        #         count+=1
        #         temp.append(n)
        # for i in range(len(temp)):
        #     nums[i]=temp[i]
        # return count
            