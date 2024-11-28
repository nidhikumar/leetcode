from typing import List 

def kthLargestElement(nums: List[int], k:int):
    k = len(nums) - k
    
    def quickSort(l, r):
        pivot = nums[r]
        p = l
        for i in range(l,r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        if p > k:
            return quickSort(l, p-1)
        elif p < k:
            return quickSort(p+1, r)
        else:
            return nums[p]

    return quickSort(0, len(nums) -1)


print(kthLargestElement([3,2,1,6,5,4], 3))