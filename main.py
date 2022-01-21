from menu import menu
from skull import skull
from login import signin, signup
import pyfiglet

def main():
    print("\Welcome\n")
    skull()

    print("\n\n────────────────────────────────────────────────\n")
    print("\t1. Login?")
    print("\t2. Register?")
    choice = int(input("\nYour choice : "))
    if choice == 1:
        test = signin()
        if (test == False):
            print(pyfiglet.figlet_format("Wrong choice"))
        else:
            menu(test)
    elif choice == 2:
        signup()
    else:
        print(pyfiglet.figlet_format("Wrong choice"))


if __name__ == '__main__':
    main()
