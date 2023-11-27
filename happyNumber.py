# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

def sum(n):
    sum = 0
    while(n != 0):
        temp = n%10
        print("temp = ",temp)
        sum = sum + (temp*temp)
        n = n//10
    print("sum = ",sum)
    
    return sum

def isHappy(n):
    n = int(n)
    happySum = sum(n)
    while len(str(happySum)) != 1:
        happySum = sum(happySum)
    if happySum == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    user_input = input("Enter a number : ")
    print(isHappy(user_input))