from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]:
        temp = []
        for i in range (0, len(words)):
            if x in words[i]:
                temp.append(i)
        return temp

if __name__ == "__main__":
     print(findWordsContaining(["abaa","sjnsas","uhier"],"a"))