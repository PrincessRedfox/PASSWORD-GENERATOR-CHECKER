# program: Password generator/checker.py
# author: Sarina Saiyed
# email: 2338323@students.carmel.ac.uk
# student number: 2338323
#
# You are to design an algorithm for your own password generator/checker with the following requirements:
#
#   To ask the user for information.
#   To give an option to either generate a password from the information input by the user.
#   To give an option to check if a password input by the user is valid

########################################################################
# Design

# To ask the user for information  
# Give user the choice to generate a password or to check an entered password is valid or not 
# If user picks to generate a password 
#   Use the information given by the user to create a password base 
#   Password must include: 
#       A set length 15 character long 
#       Include upper- and lower-case characters (letters) 
#       Number between 0-9 
#       A random generated symbol from: 
#           !,”,#,$,%,&,’,(,),*,+,,,-,.,/
# If the user chooses to check the validity of their password:
#   Allow user to enter their password
#       Check if password: 
#           Is within the set length 
#           Contain upper and lowercase characters 
#           Contains a number between 0-9 
#           Contains a symbol 
#   If the user's password contains all the requirements, output that it is a valid password 
#   If the user's password contains two to four of the requirements, output that the password is invalid and output how to improve their password 
#   If the user’s password contains  
#   one of the requirements, output that that the password is invalid and output all the requirements needed to improve their password

########################################################################
# Pseudocode

# IMPORT random 

# DEF passwordGenerator(Information): 
#   Password = Information + random.choice(Symbol) + random.choice(Symbol) + str(random.choice(Number)) 
#       RETURN Password
#
#
# DEF passwordChecker(Information): 
#   userPassword = INPUT(“Enter your password: ”) 
#   score = 0 
#   IF LEN(userPassword) < 15: 
#       For I in userPassword: 
#           If (i.islower()): 
#               Score += 1 
#           If (i.isupper()): 
#               Score += 1 
#           If (i.isdigit()): 
#               Score += 1 
#           If (I in Symbol): 
#               Score += 1 
#	END FOR LOOP 
#   ELSE: 
#       Print(“Password is too long, Password characters must be equal or less than 15”) 
#   END IF
#
#   IF Score == 5: 
#       PRINT(“Valid password”) 
#   ELIF 1 <= Score <= 4: 
#	PRINT(“Invalid password”) 
#   END IF 
#
#
#
# Information = INPUT(“Enter your information: ”) 
# Number = [0, 1, 2, 3,4, 5, 6, 7, 8, 9] 
# Symbol = [“!”,”””,”#”,“$”,”%”,”&”,“’”,”(”,”)”,“*”,”+”,”,”,“-”,”.”,”/”] 

# Option = INPUT(“Would you like to ‘generate’ a password or ‘Check’ your password? \n”) 
# WHILE Option =! ‘generate’’ or Option =! ‘check’’: 
#   IF Option == ‘generate’: 
#       passwordGenerator(Information) 
#       PRINT(passwordGenerator(Information))		 
#   ELIF Option == ‘check’: 
#       passwordChecker(Information) 
#   ELSE: 
#       PRINT(“Please write a valid input.”) 
#	END IF
# END WHILE LOOP

########################################################################
# Variables

# STR password
# STR userPassword
# INT lower
# INT upper
# INT digit
# INT symbol
# STR InformationAnimal
# STR InformationColour
# LIST Number
# LIST Symbol
# STR option

########################################################################
# Functions

# passwordGenerator
# passwordChecker

########################################################################
# Main

import random # imports the libary random



def passwordGenerator(InformationAnimal,InformationColour): # funtion for generating a password for the user
    animalIndex = InformationAnimal[0].capitalize() + InformationAnimal[-1] #takes the first and last character of animal information and joins them
    colourIndex = InformationColour[0].capitalize() + InformationColour[1] # takes first two characters of colour information
    password =  animalIndex + random.choice(Symbol) + colourIndex + random.choice(Symbol) + str(random.choice(Number)) # variable that
  # takes the input information and capitalises it as well as joining the random chosen numbers/ symbols to create a valid password
    return password # return the variable password for the user

  

def passwordChecker(): # funtion for checking an input password
    userPassword = input("Enter your password: ") # input variable
    lower, upper, digit, symbol = 0, 0 ,0 , 0 # four different variables set to 0
    if len(userPassword) < 16: # checks that the users password is not exceeding 15 characters
        for i in userPassword: # for the index i of the characters in userPassword; checks each character and goes to the next
            # the loop ends when it reaches the last character
            if (i.islower()): # checks if current index is a lower case character
                lower += 1 # if there is, variable lower is incremented by 1
            if (i.isupper()): # checks if current index is a upper case character
                upper += 1 # if there is, variable upper is incremented by 1
            if (i.isdigit()): # checks if current index is a digit character 
                digit += 1 # if there is, variable digit is incremented by 1
            if (i in Symbol): # checks if current index is a symbol character
                symbol += 1 # if there is, variable symbol is incremented by 1
            # does everthing again with the next index in userPassword 

    if (lower>=1 and upper >= 1 and digit >= 1 and symbol>=1 and lower+upper+digit+symbol==len(userPassword)): # and when all variables have run through the length of userPassword
        print("Valid input") # states valid input only if the all the requirements are more than or equal to one ^ 
    else:
        print("""Invalid input, make sure your password includes: 
 - Upper and lowercase characters
 - digits
 - symbols
 - is less than 15 characters""") # if any requrirements = 0, states invalid password and states how to imporve the password




InformationAnimal = input("Enter an animal (Up to 5 characters long): ") # input variable of first information for the generator function
InformationColour = input("Enter a colour (Up to 5 characters long): ") # input variable of the second information for the generator function

while len(InformationAnimal) > 5 or (len(InformationColour) > 5): # while loop that repeats if length of input varibles are more than 5 characters
    if len(InformationAnimal) > 5: # only repeats the animal information input
        print("Animal information should be 5 characters or less")
        InformationAnimal = input("Enter an animal (Up to 5 characters long): ")
        
    elif len(InformationColour) > 5: # only repeats the colour information input
        print("Colour information should be 6 characters or less")
        InformationColour = input("Enter a colour (Up to 5 characters long): ")
    # outputs both if both exceed 5 characters





    
    
Number = [0, 1, 2, 3,4, 5, 6, 7, 8, 9]  # stored list of numbers used for the generator funtion
Symbol = ["!","”","#","$","%","&","’","(",")","*","+",",","-",".","/"]  # stored list of valid symbols used for the generator funtion

  

option = input("Would you like to ‘generate’ a password or ‘check’ your password? \n") # allows user to either generate or check their password
while (option != 'generate' or option != 'check'): # while loop that allows the user to re-enter their options if they have chosen wrong
    if option == 'generate': 
        passwordGenerator(InformationAnimal,InformationColour) # sends user to the passwordGenerator funtion
        print(passwordGenerator(InformationAnimal,InformationColour)) # prints out the generated password using the users information
        break # ends whiile loop
    elif option == 'check':
        passwordChecker() #send user to the passwordChecker funtion
        break 
    else:
        print("Please enter a valid input") #states that the input is invalid
        option = input("Would you like to ‘generate’ a password or ‘check’ your password? \n") # allows user to re-enter their option


     
