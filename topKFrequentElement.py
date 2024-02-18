def topKFrequent(nums, k):
    # Count the frequency of each element
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    # Create a list of lists to store elements with the same frequency
    bucket = [[] for _ in range(len(nums) + 1)]

    # Place elements in the bucket based on their frequencies
    for num, freq in freq_map.items():
        bucket[freq].append(num)

    # Iterate through the bucket from the end to find the top k frequent elements
    top_k = []
    for i in range(len(bucket) - 1, 0, -1):
        if k == 0:
            break
        if bucket[i]:
            top_k.extend(bucket[i])
            k -= len(bucket[i])

    return top_k

# Example usage:
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # Output: [1, 2]
