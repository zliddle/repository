#Zilong Liddle main and cncoder

numstring = ''

def encode(numstring):
    newlist = []
    newstring = ""
    for i in range(len(numstring)):
        newlist.append(int(numstring[i]))
    final_list = [sublist + 3 for sublist in newlist]
    for i in range(len(final_list)):
        newstring = newstring + str(final_list[i])
    return newstring

def decode(encoded_password):
    # Validate the input
    if len(encoded_password) != 8 or not encoded_password.isdigit():
        return "Invalid password. Please enter an 8-digit password containing only numbers."

    # Decode each digit
    decoded_digits = []
    for digit in encoded_password:
        new_digit = (int(digit) - 3) % 10
        decoded_digits.append(str(new_digit))

    decoded_password = ''.join(decoded_digits)
    return decoded_password



#edit
if __name__ == '__main__':
    option = ""
    while option != "3":
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")
        option = input("Please enter an option: ")
        if option == "1":
            string_encode = input("Please enter your password to encode: ")
            newstring = encode(string_encode)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decodedstring = decode(newstring)
            print(f"The encoded password is {newstring}, and the original password is {decodedstring}\n")
        elif option == "3":
            break
