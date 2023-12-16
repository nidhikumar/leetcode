# def missingNumber(findArray):
#     res = len(findArray)
#     for i in range(len(findArray)):
#         res += (i - findArray[i])
#     return res

def missingNumber(findArray):
    sum1 = 0
    sum2 = 0
    for i in range(len(findArray)+1):
        sum1 += i
    for i in findArray:
        sum2 += i
    return abs(sum1 - sum2)

if __name__ == "__main__":
    findArray = [1,3,4,5,0,2,7]
    print("Missing number = ", missingNumber(findArray))