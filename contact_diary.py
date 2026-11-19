contacts = {}

def add_contact():
    name = input("Enter name: ").strip()
    number = input("Enter number: ").strip()
    contacts[name] = number
    print("---Contact Added Successfully---")

def view_contacts():
    if not contacts:
        print("no contacts in your diary")
    else:
        print("---Contact List---")
        for name, number in contacts.item():
            print(f"{name} : {number}")

def search_contacts():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    else:
        print("Contact not found")


def delete_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts :
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found")


print("---Contact Diary---")
print("1. Add contacts")
print("2. View contacts")
print("3. Search contacts")
print("4. Delete contacts")

choice = int(input("Enter your choice: "))
if choice == 1: 
    add_contact()
elif choice == 2:
    view_contacts()
elif choice == 3:
    search_contacts()
elif choice == 4:
    delete_contact()
else:
    print("Enter a valid choice.")
    