#Given a pattern and a string s, find if s follows the same pattern.
#Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

def wordPattern(pattern, s):
    arr1 = []
    arr2 = []
    for i in pattern:
        arr1.append(pattern.index(i))
    for j in s.split():
        print(j, s.split().index(j))
        arr2.append(s.split().index(j))
    print("arr1 = ",arr1)
    print("arr2 = ",arr2)
    if arr1 == arr2:
        return True
    else:
        return False

if __name__ == "__main__":
    user_input_pattern = input("Enter pattern : ")
    user_input_string = input("Enter string : ")
    print(wordPattern(user_input_pattern,user_input_string))