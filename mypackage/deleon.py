import os

def jasmine_info():
    print("Name: Jasmine Robelle De Leon")
    print("Program: Diploma in Information Technology")
    print("Age: 20")
    print("Birthday: August 4, 2004")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Alejandro")
        print("4. Comment from Esparagoza")
        print("5. Comment from Gomez")
        print("6. Comment from Mosenos")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            print("\n-- Basic Info --")
            jasmine_info ()

        elif choice == '2':
            print("\n--- Goals ---")
            print("1. Graduate with honors.")
            print("2. Obtain a fulfilling IT career.")
            print("3. Have a motorcycle.")

        elif choice == '3':
            print("\n--- Comment from Alejandro ---")
            print("---")

        elif choice == '4':
            print("\n--- Comment from Esparagoza ---")
            print("---")

        elif choice == '5':
            print("\n--- Comment from Gomez ---")
            print("---")

        elif choice == '6':
            print("\n--- Comment from Mosenos ---")
            print("---")

        elif choice == '7':
            print("\nExiting program. Goodbye!\n")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    jasmine_info()
