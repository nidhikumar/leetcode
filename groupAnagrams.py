from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))