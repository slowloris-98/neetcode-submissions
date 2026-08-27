class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #n1,n2=len(nums1), len(nums2)
        i1,i2,j = 0,0,0
        a3=[0]*len(nums1)
        while i1<m and i2<n:

            if nums1[i1]<nums2[i2]:
                a3[j]=nums1[i1]
                i1+=1
            else:
                a3[j]=nums2[i2]
                i2+=1
            j+=1
        
        while i1<m:
            a3[j]=nums1[i1]
            i1+=1
            j+=1
        
        while i2<n:
            a3[j]=nums2[i2]
            i2+=1
            j+=1

        for i in range(len(nums1)):
            nums1[i]=a3[i]