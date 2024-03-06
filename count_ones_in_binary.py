def count_ones_in_binary(number):
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return count

# Example usage:
number1 = 1011000
number2 = 10

print("Number of 1s in", number1, ":", count_ones_in_binary(number1))
print("Number of 1s in", number2, ":", count_ones_in_binary(number2))
