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
        elif option == "2"
            decodedstring = decode(newstring)
            print(f"The encoded password is {newstring}, and the original password is {decodedstring}\n")
        elif option == "3":
            break
