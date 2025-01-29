import random
import json


def join(arr, separator=''):
    # Concatenate the elements in the list using the separator
    return separator.join(map(str, arr))


#---------------------------------------------storage of data on request of user-----------------------------------------------------------------

def store(): #storing the user inputs
    
    lower = list("abcdefghijklmnopqrstuvwxyz")
    upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbs = list("0123456789")
    symbs = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    combined = lower + upper + numbs + symbs

    website = input("Enter NAME of the website: ").lower()
    username = input("Enter USERNAME: ")
    passdigits = int(input("Enter how many DIGITS of password required: "))

    # Initialize the password with one of each character type
    strongpass = (
        random.choice(lower) +
        random.choice(upper) +
        random.choice(numbs) +
        random.choice(symbs)
    )

    for i in range(0,passdigits-4):
        strongpass+= random.choice(combined)
    
    hashpass = join(random.sample(strongpass,passdigits), "") #final password
    
    #saving data as dict to string in the txt file
    newdict = {
        "website"  : website,
        "username" : username,
        "password" : hashpass
    }

    data_str=json.dumps(newdict)


    with open("password.txt", "a") as f:
        f.write(f"{data_str}\n")

    print(f"Save Successful....\nYour new generated {passdigits} digits password is ----> {hashpass} <----\n")

#---------------------------------------------retrieval of data on request of user-----------------------------------------------------------------

def retrieve():
    request = input("\nWhich website? : ").lower()

    with open("password.txt") as f:
        passlist = f.readlines()
    
    for dict in passlist:
        current_dict = json.loads(dict)
        if request == current_dict["website"]:
            print(f"\nFor {request}:\n")
            print(f"USERNAME --> {current_dict["username"]}")
            print(f"PASSWORD --> {current_dict["password"]}\n")
            return
        
    print("ERROR 404: Website NOT FOUND")

#-----------------------------------------------------------User interface---------------------------------------------------------------------------

print("\nWelcome USER to your Password Generator & Manager!\n")

def UI():
    
    print("\n [1] GENERATE and save new password")
    print("\n [2] RETRIEVE username & password\n")

    user_input=input()

    if user_input=="1":
        store()
    elif user_input=="2":
        retrieve()
    else :
        print("\nPLEASE USE ONE OF THE TWO OPTIONS")
        UI()


UI()





