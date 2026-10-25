# ------------------------------------------------------
#        Name: Jae Harrison
#       Peers: none
#  References: online text and slides
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Prompt user for a sentence until sentence contains an accepted word.
    
    Check for secret_word first, then check for dog or Dog.
    Repeat the loop if neither is found.
    """
    while True:
        #Get sentence from user
        sentence = input("Give me a sentence: ")
        #check for secret_word
        if secret_word in sentence:
            print("You used the secret word!")
            return
        #if not, check for dog/Dog
        elif "dog" in sentence or "Dog" in sentence:
            print('You used the word "dog" or the word "Dog"!')
            return
        #if none of the words are used, repeat
        else:
            print("Try again")

#my two main problems were not correctly typing the print outs for Tasks 1 and 2, so pretty easy fixes

# Task 2
def check_greater():
    """ Read two integers and compare them.
    
    If the integers are equal, repeat inputs.
    When they are unequal (1 integer is greater than the other), stop.
    """
    while True:
        #get two integers from user
        first = int(input("Give me one integer: "))
        second = int(input("Give me a second integer: "))
        #Compare values and stop if they are unequal
        if first > second:
            print("First is Greater")
            return
        elif second > first:
            print("Second is Greater")
            return
        else:
            #in case int inputs are equal
            print("Try again")



# Task 3
def get_special_numbers():
    """ Print odd multiples of 3 from 1 to 40, excluding multiples of 5.
    """
    #read every integer from 1 through 40
    for num in range(1,41):
        #skip even numbers(to isolate odd multiples)
        if num % 2 == 0:
            continue
        #skip numbers that are non-multiples of 3
        if num % 3 != 0:
            continue
        #skip numbesr that are multiples of 5
        if num % 5 == 0:
            continue
        #print numbers that fulfill all conditions
        print(num)



# Task 4.a
def my_for_loop():
    """ Read a string input from the user and classify each character
    
    If inputted string has spaces or a length outside 2-5 characters,reject and try again
    If that is not the case, print whether each character is a vowel or a consonant
    """
    #prompt user to input a string
    word = input("Give me a string: ")
    #reject string if it has spaces or invalid length
    if len(word) < 2 or len(word) > 5 or " " in word:
        print("bad word")
        return
    #determine vowels, upper and lower case
    vowels = "aeiouAEIOU"
    for letter in word:
        if letter in vowels:
            print(f"letter {letter} is a vowel")
        else:
            print(f"letter {letter} is a consonant")


# Task 4.b
def my_while_loop():
    """ Give a menu that repeats until user inputs (selects) b or c

    Options actions: a - repeat the menu, b - print Goodbye and return, c - exit the program
    Invalid inputs (other letters etc.) print try again
    """
    while True:
        #Ask the user to select an option
        option = input("Choose one option: a, b, or c: ")
        #if a, loop and repeat menu
        if option == "a":
            continue
        #if b, bye and end loop
        elif option == "b":
            print("Goodbye")
            return
        #if c, exit program
        elif option == "c":
            sys.exit()
        #if invalid, repeat menu
        else:
            print("try again")
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

#Do not modify
if __name__ == "__main__":
    main()
    print("The End")
