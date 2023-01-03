contact = {"Amit": 3562149861,
           "Harry": 9363938525,
           "Sonam": 9966852372,
           "Bhumi": 8896385210,
           "Falguni": 7722963852
           }

while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3.Display contacts\n 4. Edit contact \n 5. Delete contact\n 6.Exit\n Enter your choice: "))
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = int(input("Enter the mobile number: "))
        contact[name] = phone
        print("Contact successfully added")
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name, "'s contact number is ", contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        for number in contact:
            print("Name:{},Number:{}".format(number, contact[number]))
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited: ")
        if edit_contact in contact:
            phone = input("Enter mobile number: ")
            contact[edit_contact] = phone
            print("Contact updated")

        else:
            print("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='y' or confirm =='Y':
                contact.pop(del_contact)
            print("Contact succesfully deleted")
        else:
            print("Name is not found in contact book")
    else:
        break
