import random


# Basic password generator by Kieran. B. Doherty
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "'!@#$%^&*()_-+=:;{[]}\|/?,.<>"
numbers = "0123456789"

string = lower + upper + numbers + symbols
length = 16
thepassword = "".join(random.sample(string,length))


print("Your new password is : " + thepassword)



save = input("Do you want to save the password to a text file? [y/n]")

if save == "y":
    with open("passwords.txt", "a") as f:
        f.write("password :" + thepassword + "\n")
elif save == "n":
    quit()

else:
    print("Please pick a valid option")
        



