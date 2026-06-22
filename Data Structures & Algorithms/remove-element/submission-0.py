class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp=[]
        count=0
        for n in nums:
            if n!=val:
                count+=1
                temp.append(n)
        for i in range(len(temp)):
            nums[i]=temp[i]
        return count
            