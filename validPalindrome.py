def main(str):
    s1 = ''
    for c in str.lower():
        if c.isalnum():
            s1 += c
    return True if s1 == s1[::-1] else False

if __name__ == "__main__":
    print(main("A man, a plan, a canal: Panama"))