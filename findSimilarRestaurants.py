def findSimilarRestaurants(name, restaurant_list):
    def are_similar(name1, name2):
        if len(name1) != len(name2):
            return False
        diff_indices = [i for i in range(len(name1)) if name1[i] != name2[i]]
        if len(diff_indices) == 0:  # Already identical
            return True
        if len(diff_indices) == 2:  # Check if swapping makes them identical
            i, j = diff_indices
            return name1[i] == name2[j] and name1[j] == name2[i]
        return False

    return [r for r in restaurant_list if are_similar(name, r)]

# Tests
input_name = "hotpot"
restaurant_list = ["hottop", "hotopt", "hotpit", "httoop", "hptoot"]
print(findSimilarRestaurants(input_name, restaurant_list))  # ["hottop", "hotopt", "hptoot"]

input_name = "biryani"
restaurant_list = ["biryani", "biryeni", "biriyani", "biriany", "briynai"]
print(findSimilarRestaurants(input_name, restaurant_list))  # ["biryani", "biriany"]

input_name = "omega grill"
restaurant_list = ["omeag grill", "omeea grill", "omega gril", "omegla gril"]
print(findSimilarRestaurants(input_name, restaurant_list))  # ["omeag grill"]
