def containsDuplicate(nums: list[int]) -> bool:
    return (len(nums)==len(set(nums)))


if __name__ == "__main__":
    array = [1,2,3,4,1]
    val = containsDuplicate(array)
    print(val)