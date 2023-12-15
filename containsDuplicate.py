def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        else:
            hashset.add(n)
    return False

if __name__ == "__main__":
    array = [1,2,3,4,1]
    val = containsDuplicate(array)
    print(val)