def print_menu():  # print menu function for all inputs
    print('1. Print Phone Numbers')  # starting value to print a number but only works when there is a value in dict
    print('2. Add a Phone Number')  # starting value to add a number
    print('3. Remove a Phone Number')  # starting value to remove a number but only when there is a value in dict
    print('4. Lookup a Phone Number')  # starting value to lookup a number but only when there is a value in dict
    print('5. End Task')  # breaks out of loop and displays starting value again


numbers = {}  # dictonary where every name and number will be stored
menu_choice = 0  # menu_choice assigned to 0 to convert string to int
print_menu()  # functions for adding removing etc.
while menu_choice != 5:  # while loop so the program loops forever until the user wants to break outside the loop
    menu_choice = int(input("Type in a number (1-5): "))  # integer input so the user cannot input a string
    if menu_choice == 1:  # loop for when the user wants to Print numbers in dict
        print("Telephone Numbers:")  # spit out all values stored in dict
        for dictkeys in numbers.keys():  # for loop
            print("Name: ", dictkeys, "\tNumber:", numbers[dictkeys])  # print all nums in dictionary. \t means tab
        print()   # print all nums in dictionary. \t means tab
    elif menu_choice == 2:  # second loop to add a number in the dict
        print("Add Name and Number")  # prompt
        name = input("Name: ")  # asks user to input name and assigns the input to the variable "name"
        phonenum = int(input("Number: "))  # Asks user for a number and saves input to variable called phone
        numbers[name] = phonenum  # pushes all data to a dict
    elif menu_choice == 3:  # is user wants to remove a name then they will be directed here
        print("Remove Name and Number")  # will show user what is happening
        name = input("Name: ")  # will look through all names and find if names match
        if name in numbers:  # if the name is in the dict numbers
            del numbers[name]  # then delete the name from the dict numbers
        else:
            print(name, "was not found")  # if name is not in name
    elif menu_choice == 4:  # if user wants to lookup a name
        print("Lookup Number")  # then we will prompt user on the operation
        name = input("Name: ")  # take input from user and search through name.
        if name in numbers:  # and if we find the exact name in the dict
            print("The number is", numbers[name])  # then we will print out saying what we have found
        else:
            print(name + "was not found")  # if not found we will tell the user that the name was not found
    elif menu_choice != 5:
        print_menu()


# common errors/problems

# common error received was the string to int conversion as i was doing "+" instead of ,"
# properly spacing the loops and functions which gave many errors
# menu choices where not showing up as it needed to be specified as " else if(elif) menu_choices does not equal 5 because
# if the != was not present than the loop would display the options and break.
