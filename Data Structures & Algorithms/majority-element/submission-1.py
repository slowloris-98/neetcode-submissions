class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        maj_count=1
        maj_ele=nums[0]
        for j in range(0,len(nums)):
            if nums[j]!=nums[i]:
                i=j
            else:
                if maj_count<j-i+1:
                    maj_ele=nums[i]
                    maj_count=j-i

        return maj_ele
            
            


