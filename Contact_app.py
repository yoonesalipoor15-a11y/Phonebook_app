#Dinfine a dictionary with a specific value to store contact information
phone_book = {
    "sara" : ["09011111111"]
}

#Main menu of the program
menu_text = """
---Phonebook---
1-Add contact
2-Add number to contact
3-Search phone number by name
4-Delete contact
5-Number of contact
6-Exit"""

#Infinite loop for program execution
while True :

    user_choice = input(menu_text)

    result_message = ""

    if user_choice in ("6",""):
        print("Goodbye!")
        break

    if user_choice == "1" :
        name = input("Enter the contact's name: ").strip().lower()
        if name in phone_book:
            result_message += "A contact with this name already exists."

        else:
            number = input("Enter phone number: ")    
            phone_book[name] = [number]
            result_message += "Contact added successfully."

    elif user_choice == "2" :
        name = input("Enter the contact's name: ").strip().lower()
        existing_numbers = phone_book.get(name)

        if existing_numbers is not None:
            number = input("Enter the new number: ")
            phone_book[name].append(number)
            result_message += "New number added."

        else:
            result_message += "No contact with this name found."
        
    elif user_choice == "3" :
        name = input("Enter the contact's name: ").strip().lower()
        existing_numbers = phone_book.get(name)

        if existing_numbers is not None:
            result_message += str(phone_book[name])

        else:
            result_message += "No contact with this name found."

    elif user_choice == "4" :
        name = input("Enter the contact's name: ").strip().lower()
        if name in phone_book :
            del phone_book[name]
            result_message += "Contact deleted successfully."
        else :
            result_message += "No contact with this name found."    

    elif user_choice == "5" :
        result_message += "Number of contacts: " + str(len(phone_book))
        
    #Handling invalid input    
    else:
        result_message = "The input must be a value between 1 and 6."
    print(result_message)   
    keep_going = True 
    while True :
        cont = input("Do you want to continue? (Yes/No): ") 
        if cont in ("No", "no", "n", ""):
            print("Goodbye!")
            keep_going = False
            break
        elif cont in ("Yes", "yes", "y"):
            print()
            break
        else:
            print("Please answer with Yes or No.")
    if keep_going == False :
        break
