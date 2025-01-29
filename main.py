import random


def join(arr, separator=''):
    # Concatenate the elements in the list using the separator
    return separator.join(map(str, arr))



# Character sets
lower = list("abcdefghijklmnopqrstuvwxyz")
upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbs = list("0123456789")
symbs = list("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

# Correct combined list
combined = lower + upper + numbs + symbs

print("\nWelcome USER to your password generator!\n")

website = input("Enter NAME of the website: ")
link = input("Enter LINK: ")
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
    
hashpass = join(random.sample(strongpass,passdigits), "")


with open("password.txt", "a") as f:
    f.write(f"{website} | {link} | {hashpass}\n")
