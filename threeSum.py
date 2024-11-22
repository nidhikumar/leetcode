def threeSum(nums,target):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threesum = a + nums[l] + nums[r]
            if threesum > target:
                r -= 1
            elif threesum < target:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1


    return res  


if __name__ == "__main__":
    nums = [2,7,11,13,0]
    target = 9
    res = threeSum(nums,target)
    print(res)