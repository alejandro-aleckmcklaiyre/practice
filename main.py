from package import deleon

def main_menu():
    while True:
        print("\n--------Main Menu -------")
        print("[1] Aleck Mcklaiyre Alejandro")
        print("[2] Jasmine Robelle De leon")
        print("[3] Mikka Kette Esparagoza")
        print("[4] Ashley Hermoine Gomez")
        print("[5] Loise Nicole Mosenos")
        print("[6] Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            alejandro.aleck_info()

        elif choice == '2':
            deleon.jasmine_info()
            
        elif choice == '3':
            esparagoza.esparagoza_menu()

        elif choice == '4':
            gomez.menu()

        elif choice == '5':
            mosenos.mosenos_info()  

        elif choice == '6':
            print("\nExiting program.\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

if __name__ == "__main__":
    main_menu()