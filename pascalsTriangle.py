def pascalsTriangle(nums):
    res = [[1]]
    for i in range (nums - 1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res  


if __name__ == "__main__":
    nums = 5
    res = pascalsTriangle(nums)
    print(res)


# 1, 1, 1, 1, 2, 1, 1, 3, 3, 1