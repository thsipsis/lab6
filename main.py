#Main function and encode function written by Theofanis Sipsis

#Our password
pw = ""

#We assume that these are valid numbers, no error/exception checking
def encode(s):
    #reset our password
    global pw
    pw = ""
    for c in s:
        c = (int(c) + 3) % 10
        pw = f"{pw}{c}"

def main():
    #Our eternal loop
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        op = input("Please enter an option: ")
        if op == "1":
            encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif op == "2":
            print(pw)
        #We'll just quit on any invalid input or 3, assignment doesn't mention
        #we need to handle invalid input
        else:
            break
        print()

if __name__ == "__main__":
    main()
