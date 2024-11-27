from collections import Counter

def findKAnagrams(name, restaurant_list, k):
    def is_k_anagram(name1, name2, k):
        if len(name1) != len(name2):
            return False
        count1, count2 = Counter(name1), Counter(name2)
        differences = sum((count1 - count2).values())
        return differences <= k

    return [r for r in restaurant_list if is_k_anagram(name, r, k)]

# Tests
input_name = "anagram"
restaurant_list = ["grammar", "grammer", "anagram"]
K = 2
print(findKAnagrams(input_name, restaurant_list, K))  # ["grammar", "anagram"]

input_name = "anagram"
restaurant_list = ["grammar"]
K = 3
print(findKAnagrams(input_name, restaurant_list, K))  # ["grammar"]

input_name = "anagram"
restaurant_list = ["grammar"]
K = 1
print(findKAnagrams(input_name, restaurant_list, K))  # []

input_name = "omexyb grillg"
restaurant_list = ["omgxca grille"]
K = 2
print(findKAnagrams(input_name, restaurant_list, K))  # ["omgxca grille"]
