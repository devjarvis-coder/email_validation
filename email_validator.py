email = input(" Enter your email: ")
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        print("whitespace in your email")
                    elif i.isalpha():
                        if i == i.isupper():
                            print("uppercase in your email")
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        print("wrong email address")
            else:
                print("email structure is wrong")
        else:
            print("@ is not available")
    else:
        print("email first character is not alphabet")
else:
    print("email length is short")
