from typing import List

def finalValueAfterOperations(operations: List[str]) -> int:
        temp = 0
        for i in range (0,len(operations)):
            if operations[i] == "--X" or operations[i] == "X--":
                temp -= 1
            else:
                temp += 1
        return temp

if __name__ == "__main__":
    arr = ["--X","X++","X++"]
    print(finalValueAfterOperations(arr))
