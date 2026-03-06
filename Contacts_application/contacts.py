import re

phonebook = {}
total_budget = 0

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def calculate_priority(relationship):
    priority_map = {
        "Family": 5,
        "Close Friend": 4,
        "Friend": 3,
        "Colleague": 2,
        "Other": 1
    }
    return priority_map.get(relationship, 1)


def add_contact():
    global total_budget
    phone = input("Enter Contact Number (10 digits number): ")

    if not validate_phone(phone):
        print("Invalid Phone Number!")
        return

    if phone in phonebook:
        print("Duplicate Entry Not Allowed!")
        return

    name = input("Enter Name: ").title()
    email = input("Enter Email: ")

    if not validate_email(email):
        print("Invalid Email Format!")
        return

    relationship = input("Enter Relationship (Family/Close Friend/Friend/Colleague/Other): ")
    location = input("Enter House Location: ")
    return_gift = input("Enter Return Gift: ")
    gift_cost = float(input("Enter Gift Cost: "))
    
    priority = calculate_priority(relationship)

    phonebook[phone] = {
        "name": name,
        "email": email,
        "relationship": relationship,
        "location": location,
        "return_gift": return_gift,
        "gift_cost": gift_cost,
        "priority": priority
    }

    total_budget += gift_cost

    print("💌 Contact Added Successfully!")


def search_number():
    phone = input("Enter Contact Number: ")

    if phone in phonebook:
        print(phonebook[phone])
    else:
        print("Contact Not Found!")


def search_name():
    name = input("Enter Name to Search: ").title()
    found = False

    for phone, details in phonebook.items():
        if details["name"] == name:
            print(phone, details)
            found = True

    if not found:
        print("Contact Not Found!")

def search_location():
    location = input("Enter Location to Search: ")
    found = False

    for phone, details in phonebook.items():
        if details["location"] == location:
            print(phone, details)
            found = True

    if not found:
        print("Contact Not Found!")

def filter_relationship():
    category = input("Enter Realtionship to Filter: ")
    found = False

    for phone, details in phonebook.items():
        if details["relationship"] == category:
            print(phone, details)
            found = True

    if not found:
        print("No Contacts Found!")


def vip_contact():
    print("\n VIP GUEST LIST ")
    for phone, details in phonebook.items():
        if details["priority"] >= 4:
            print(phone, details)


def total_gift_budget():
    print("Total Return Gift Budget:", total_budget)


def delete_contact():
    global total_budget

    phone = input("Enter Contact Number to Delete: ")

    if phone in phonebook:
        total_budget -= phonebook[phone]["gift_cost"]
        del phonebook[phone]
        print("Contact Deleted Successfully!")
    else:
        print("Contact Not Found!")


def display_contacts():
    if not phonebook:
        print("Phonebook is Empty!")
        return

    for phone, details in phonebook.items():
        print("\nContact:", phone)
        for key, value in details.items():
            print(f"{key}: {value}")
        print("---------------------------")

while True:
    print("\n  *******SMART INVITE CONTACTS******* ")
    print("1.  Add Contact")
    print("2.  Search by Number")
    print("3.  Search by Name")
    print("4.  Filter by Realtionship")
    print("5.  Search by Location")
    print("6.  Display VIP Contacts")
    print("7.  Total Gift Budget")
    print("8.  Delete Contact")
    print("9.  Display All Contacts")
    print("10. 📩 Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_number()
    elif choice == "3":
        search_name()
    elif choice == "4":
        filter_relationship()
    elif choice == "5":
        search_location()
    elif choice == "6":
        vip_contact()
    elif choice == "7":
        total_gift_budget()
    elif choice == "8":
        delete_contact()
    elif choice == "9":
        display_contacts()
    elif choice == "10":
        print("Exiting.")
        break
    else:
        print("Invalid Choice!")