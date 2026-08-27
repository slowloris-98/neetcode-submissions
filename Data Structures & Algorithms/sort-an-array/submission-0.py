class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums)-1)
        print(nums)
        return nums
        

    def mergeSort(self, arr, low, high):
        if low<high:
            mid=(low+high)//2
            self.mergeSort(arr, low, mid)
            self.mergeSort(arr, mid+1, high)
            self.merge(arr, low, mid, high)


    def merge(self, arr, low, mid, high):
        i1,i2 = 0, 0
        left=arr[low:mid+1]
        right=arr[mid+1:high+1]
        n1,n2 = len(left), len(right)

        #a3=[0]*(n1+n2)
        j=low
        while i1<n1 and i2<n2:
            if left[i1]<right[i2]:
                arr[j] = left[i1]
                i1+=1
            else:
                arr[j] = right[i2]
                i2+=1
            j+=1

        while i1<n1:
            arr[j]=left[i1]
            i1+=1
            j+=1
        
        while i2<n2:
            arr[j]=right[i2]
            i2+=1
            j+=1
        