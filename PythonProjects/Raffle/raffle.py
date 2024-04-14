class Raffle:
    def __init__(self):
        self.entries = set()

    def add_entry(self, name):
        # Convert the name to lowercase to ensure case-insensitive storage
        self.entries.add(name.lower())

    def is_entry_present(self, name):
        # Check if the lowercase version of the name is present in the set
        return name.lower() in self.entries

    def get_entries(self):
        # Return the entries in their original case
        return self.entries

    def clear_entries(self):
        # Clear all entries
        self.entries.clear()

def main():
    raffle = Raffle()
    print("Welcome to the Raffle Program!")

    while True:
        print("\nMenu:")
        print("1. Add entry")
        print("2. Check entry")
        print("3. Show all entries")
        print("4. Clear all entries")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name to add: ")
            raffle.add_entry(name)
            print("Entry added successfully!")

        elif choice == '2':
            name = input("Enter the name to check: ")
            if raffle.is_entry_present(name):
                print(f"{name} is present in the raffle.")
            else:
                print(f"{name} is not present in the raffle.")

        elif choice == '3':
            entries = raffle.get_entries()
            if entries:
                print("Entries in the raffle:")
                for entry in entries:
                    print(entry)
            else:
                print("No entries in the raffle.")

        elif choice == '4':
            raffle.clear_entries()
            print("All entries cleared.")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
