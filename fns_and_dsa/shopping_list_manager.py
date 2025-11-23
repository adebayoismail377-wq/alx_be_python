def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View Shopping List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            item = input("Enter Item to Add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"{item} added to the list.")
            else:
                print("Item cannot be empty.")

        elif choice == "2":
            item = input("Enter Item to Remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print("Item not found in the list.")

        elif choice == "3":
            if shopping_list:
                print("Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Shopping List is empty.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
  