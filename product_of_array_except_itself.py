from typing import List


def product(nums: List[int]):
    # nums = [1, 2, 3, 4, 5]
    array = [1] * len(nums)
    for i in range(1, len(nums)):
        array[i] = array[i-1] * nums[i-1]
    right = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        array[i] = array[i] * right
        right = right * nums[i]
    return array

if __name__ == "__main__":
    nums = [1,2,3,4]
    result = product(nums)
    print("Result = ",result)


