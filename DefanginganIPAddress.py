def defangIPaddr(address: str) -> str:
    return address.replace(".","[.]")

if __name__ == "__main__":
    user_input_s = input("enter IP address : ")
    print(defangIPaddr(user_input_s))
