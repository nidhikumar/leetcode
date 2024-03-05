from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
        temp = {}
        for i in nums:
            if i in temp:
                temp[i] = temp[i]+1
            else:
                temp[i] = 1
        sum = 0
        for i in temp:
            n = temp[i]
            if n > 1:
                sum = sum + (n*(n-1))/2
        return int(sum)

if __name__ == "__main__":
     print(numIdenticalPairs([1,2,1,1,3,2]))