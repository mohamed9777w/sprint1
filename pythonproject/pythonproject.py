import csv
import datetime
import os
import re
import datetime
import shutil
CSV_FILE = "contactbook.csv"
# Get the current date
current_date = datetime.datetime.now().strftime("%d%m%Y")

# Set the filename with the current date
current_file = f"contactbook_{current_date}.csv"

# Set to store usernames
existing_usernames = set()

# Create a new contact and add it to the CSV file
def create_contact():
    global existing_usernames
    while True:
        username = input("Enter username: ")
        contacts = []
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, "r") as file:
                reader = csv.reader(file)
                contacts = list(reader)
                existing_usernames = set(contact[0] for contact in contacts)

        if username in existing_usernames:
            print("Username already exists. Please enter a different username.")
            continue
        
        
        # Validate email
        while True:
            email = input("Enter email: ")
            if re.match(r'^[\w.-]+@[\w.-]+(\.[\w]+)+$', email):
                break
            else:
                print("Invalid email format. Please enter a valid email.")

        # Validate phone numbers
        while True:
            phone_numbers = input("Enter phone numbers (comma-separated): ")
            numbers = phone_numbers.split(",")
            valid_numbers = True
            for number in numbers:
                if not re.match(r'^\d{11}$', number.strip()):
                    valid_numbers = False
                    break
            if valid_numbers:
                break
            else:
                print("Invalid phone number format. Please enter valid 11-digit numbers separated by commas.")
        
        address = input("Enter address: ")
        
        insertion_date = datetime.datetime.now().strftime("%d%m%Y")
        contact = [username, email, ','.join(numbers), address, insertion_date]
        
        
        with open(CSV_FILE, "a", newline='') as file:
           writer = csv.writer(file)
           writer.writerow(contact)
 

        print("Contact created successfully!")
        
        choice = input("Do you want to enter another contact? (y/n): ")
        if choice.lower() != 'y':
            break

# Update an existing contact in the CSV file
def update_contact():
    global existing_usernames  # Declare existing_usernames as a global variable

    username = input("Enter username of the contact to update: ")

    contacts = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)

    existing_usernames = set(contact[0] for contact in contacts)

    updated = False
    for contact in contacts:
        if contact[0] == username:
            while True:
                print("Select field to update:")
                print("1. Username")
                print("2. Address")
                print("3. Email")
                print("4. Phone")
                print("0. Back to the main menu")
                choice = input("Enter your choice (1-4): ")

                if choice == "1":
                    new_username = input("Enter new username: ")
                    if new_username in existing_usernames and new_username != username:
                        print("Username already exists. Please enter a different username.")
                        continue
                    else:
                        contact[0] = new_username
                        updated = True
                elif choice == "2":
                    new_address = input("Enter new address: ")
                    contact[3] = new_address
                    updated = True
                elif choice == "3":
                    while True:
                        new_email = input("Enter new email: ")
                        if not re.match(r'^[\w.-]+@[\w.-]+(\.[\w]+)+$', new_email):
                            print("Invalid email format. Please enter a valid email.")
                            choice = input("Do you want to enter the email again? (y/n): ")
                            if choice.lower() != 'y':
                                break
                        else:
                            contact[1] = new_email
                            updated = True
                            break
                elif choice == "4":
                    while True:
                        new_phone_numbers = input("Enter new phone numbers (comma-separated): ")
                        numbers = new_phone_numbers.split(",")
                        valid_numbers = all(re.match(r'^\d{11}$', number.strip()) for number in numbers)
                        if not valid_numbers:
                            print("Invalid phone number format. Please enter valid 11-digit numbers separated by commas.")
                            choice = input("Do you want to enter phone numbers again? (y/n): ")
                            if choice.lower() != 'y':
                                break
                        else:
                            contact[2] = ','.join(numbers)
                            updated = True
                            break
                elif choice == "0":
                    break
                else:
                    print("Invalid choice. Please try again.")
                    continue

                break

    if updated:
        with open(CSV_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

        choice = input("Do you want to enter another username? (y/n): ")
        if choice.lower() == 'y':
            update_contact()

# Delete a contact from the CSV file
def delete_contact():
    username = input("Enter username of the contact to delete: ").strip().lower()
    
    contacts = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)
    
    deleted = False
    updated_contacts = []
    for contact in contacts:
        if contact[0].strip().lower() != username:
            updated_contacts.append(contact)
        else:
            deleted = True
    
    if deleted:
        with open(CSV_FILE, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_contacts)
        
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# List all contacts in the CSV file
def list_contacts():
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r") as file:
            reader = csv.reader(file)
            contacts = list(reader)

        for contact in contacts:
            print(f"Username: {contact[0]}")
            print(f"Email: {contact[1]}")
            print(f"Phone Numbers: {contact[2].split(',')}")
            print(f"Address: {contact[3]}")
            print(f"Insertion Date: {contact[4]}")
            print("")
# Backup the contactbook CSV file
def backup_contactbook():
    if os.path.exists(CSV_FILE):
        shutil.copy2(CSV_FILE, current_file)
        print(f"Contactbook backed up as {current_file}")
# User menu for selecting operation
def user_menu():
    while True:
        print("----- Contact Book Menu -----")
        print("1. Create contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. List contacts")
        print("0. Exit")
        
        choice = input("Enter your choice (0-4): ")
        
        if choice == "1":
            create_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            list_contacts()
        elif choice == "0":
            break
       
        else:
            print("Invalid choice. Please try again.")
        # Backup contactbook after each operation
        backup_contactbook()
# Call the user_menu function to start the program
user_menu()

