import random

#this dictionary contains the substitution keys and their values 
subs = {'A': '@', 'a': '*', 
        'I': '1', 'i': '!',}
#randomly picks 1 or 2 substitutions to make in the user's responses, with a preference towards only 1
num_to_replace = random.randrange(1, 2, 1)
#list to check the characters of the string against
substitutions = ['A', 'a', 'I', 'i']

#the introductory function. does several things: 
#   introduces the program, what it does, and how it works
#   gets the data from the user to generate their password
def introduction():
    intro = "----\n The purpose of this program is to generate a strong, easy to remember password.\n Simply answer the following prompts and remember to keep them not too short and not too long. A longer password is better, until it becomes too long.\n----\n"
    print(intro)

    #prompts
    user_application = str(input("What application, service, or device is this password for?  "))
    
    user_name = str(input("\nWhat is your first name or nickname?  "))
    #checks if the user's "user_name" response is less than 4 characters
    while len(user_name) < 4:
        print("   Please enter more than 4 characters.")
        user_name = str(input("\nWhat is your first name or nickname?  "))
    user_fav_num = str(input("\nWhat is your favorite number?  "))
    
    pwd_len = int(input("\nApproximately how many characters long would you like your password to be?  "))
    #checks if the user's "pwd_len" response is less than 6 characters
    while pwd_len < 6:
        print("   Be careful! No matter the application, service, or device you're using, it is never a good idea to use a short password. Try again!")
        pwd_len = int(input("Approximately how many characters long would you like your password to be?  "))
    if pwd_len <= 8:
        user_pwd = user_name.upper() + str(user_fav_num)
    elif pwd_len >= 8 or pwd_len <= 12:
        user_pwd = user_name.upper() + user_application
    else:
        user_pwd = user_name.upper() + user_application + str(user_fav_num)

    #calls the next step, the substitutions function
    substitution(user_pwd, subs, substitutions)

#the substitutions function
def substitution(user_pwd, subs, substitutions):
    for letter in substitutions:
        if letter in user_pwd:
            user_pwd = user_pwd.replace(letter, subs[letter], num_to_replace)
    user_pwd = user_pwd + "#"
    print("\n\nYour password is: " + user_pwd + "\n")

#initializes the whole program
introduction()






