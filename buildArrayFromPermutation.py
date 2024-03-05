from typing import List


def buildArray(nums: List[int]) -> List[int]:
        temp = []
        for i in range (0,len(nums)):
            temp.append(nums[nums[i]])
        return temp

if __name__ == "__main__":
      nums = [0,2,1,3,4,5]
      print(buildArray(nums))