# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# def validAnagram(s, t):
#     dictionary = {}
#     for char in t:
#         if char not in dictionary:
#             dictionary[char] = 1
#         else:
#             dictionary[char] += 1
#     for char in s:
#         if char in dictionary and dictionary[char] > 0 and len(s)==len(t):
#             dictionary[char] -= 1
#         else:
#             return False
#     return True

#alternate solution

def validAnagram(s,t):
    if len(s) != len(t):
        return False
    for char in set(s):
        if s.count(char) != t.count(char):
            return False
    return True

if __name__ == "__main__":
    user_input_s = input("enter s : ")
    user_input_t = input("enter t : ")
    print(validAnagram(user_input_s,user_input_t))

    