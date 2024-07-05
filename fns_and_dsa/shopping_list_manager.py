def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def main ():
    shopping_list = []
    while True:
        choice = input("[Enter your choice:]")
        if choice == '1':
           item = input(["Enter the item to add:"])
           shopping_list.append(item)
           print(f"{item} added to the list.")
        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from the list.")
            else:
                print(f"{item} not found in the list.")
        elif choice == '3':
            if shopping_list:
                print("Your Shopping List:")
                for item in shopping_list:
                    print(item)
            else:
                print("The list is currently empty.")
        elif choice == '4':
            print("Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
   main()
