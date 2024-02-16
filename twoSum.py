def twoSum(nums,target):
    numSet = {}
    res = []
    for i in range(len(nums)):
        if (target-nums[i]) in numSet:
            res.append(i)
            res.append(numSet[target-nums[i]])
        numSet[nums[i]] = i
    return res  


if __name__ == "__main__":
    nums = [2,7,11,13]
    target = 9
    res = twoSum(nums,target)
    print(res)