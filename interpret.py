def interpret(textString):
    res = ""
    i = 0
    while i < len(textString):
        if textString[i:i+2] == "()":
            res += "o"
            i += 2
        elif textString[i] == "(":
            start = i + 1
            while i < len(textString) and textString[i] != ")":
                i += 1
            res += textString[start:i]
            i += 1
        else:
            res += textString[i]
            i += 1
    return res 


if __name__ == "__main__":
    res = interpret(textString="g()()(al)")
    print(res)