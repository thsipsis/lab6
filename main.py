## Main function and encode function written by Theofanis Sipsis

# Our password
pw = ""
original_pw = ""

# We assume that these are valid numbers, no error/exception checking
def encode(s):
    global pw, original_pw
    original_pw = s  # Store the original password
    pw = ""
    for c in s:
        c = (int(c) + 3) % 10
        pw = f"{pw}{c}"

def decode(s):
    decoded_pw = ""
    for c in s:
        c = (int(c) - 3) % 10  # Shift back by 3
        decoded_pw = f"{decoded_pw}{c}"
    return decoded_pw

def main():
    # Our eternal loop
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        op = input("Please enter an option: ")
        if op == "1":
            password_input = input("Please enter your password to encode: ")
            encode(password_input)
            print("Your password has been encoded and stored!")
        elif op == "2":
            if pw:  # Check if there's a password to decode
                decoded_password = decode(pw)
                print(f"Encoded password: {pw}, and the original password is: {original_pw}")
            else:
                print("No password has been encoded yet.")
        else:
            break
        print()

if __name__ == "__main__":
    main()