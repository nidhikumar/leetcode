def squareRoot(x: int)-> int:
    l,r = 0,x
    res = 0
    while(l<=r):
        m = l + ((r-l)//2)
        if m ** 2 > x:
            r = m - 1
        elif m ** 2 < x:
            l = m + 1
            res = m
        else:
            return m
    return res

if __name__ == "__main__":
    x = input("Enter a number: ")
    print("Square root of ", x ," = ", squareRoot(int(x)))