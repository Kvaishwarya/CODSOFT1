class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} | {self.phone} | {self.email} | {self.address}"

#contcatmanger 
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
            return
        for contact in found_contacts:
            print(contact)

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number (leave blank to skip): ")
            new_email = input("Enter new email (leave blank to skip): ")
            new_address = input("Enter new address (leave blank to skip): ")
            manager.update_contact(name, new_phone if new_phone else None, new_email if new_email else None, new_address if new_address else None)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()