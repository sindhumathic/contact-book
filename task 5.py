class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}, {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Added contact: {contact}")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        results = [c for c in self.contacts if search_term in c.name or search_term in c.phone]
        if results:
            for contact in results:
                print(contact)
        else:
            print("No contacts found.")

    def update_contact(self, name, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = new_phone or contact.phone
                contact.email = new_email or contact.email
                contact.address = new_address or contact.address
                print(f"Updated contact: {contact}")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Deleted contact: {contact.name}")
                return
        print("Contact not found.")


def main():
    manager = ContactManager()
    
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
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
            new_phone = input("Enter new phone (leave blank to keep current): ")
            new_email = input("Enter new email (leave blank to keep current): ")
            new_address = input("Enter new address (leave blank to keep current): ")
            manager.update_contact(name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
