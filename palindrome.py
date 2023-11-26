def main(str):
    if str == str[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    str = input("Enter string")
    print(main(str))