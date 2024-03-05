def numJewelsInStones(jewels: str, stones: str) -> int:
    return sum([stones.count(j) for j in jewels])

if __name__ == "__main__":
    print(numJewelsInStones("aA","aAAbbbb"))