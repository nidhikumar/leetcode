#Given two strings ransomNote and magazine
#return true if ransomNote can be constructed by using the letters from magazine 
#and false otherwise.

def ransomeNote(ransomenote, magazine):
    dictionary = {}
    for char in magazine:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    for char in ransomenote:
        if char in dictionary and dictionary[char] > 0:
            dictionary[char] -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    user_input_ransomenote = input("Enter ransome note value : ")
    user_input_magazine = input("Enter magazine value : ")
    print(ransomeNote(user_input_ransomenote,user_input_magazine))

