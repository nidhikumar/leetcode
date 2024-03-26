def numberLessThanEachNumber(num):
    num = sorted(num)
    return [num.index(x) for x in num]


if __name__ == "__main__":
    num = [2,7,11,13,15,2,7]
    res = numberLessThanEachNumber(num)
    print(res)