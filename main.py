from getout import getout
from menu import menu
from skull import skull


def main():
    print("\n──────────────────Welcome hacker──────────────────\n")
    skull()

    print("\n\n──────────────────Identify yourself──────────────────\n")
    print("\t1. Login")
    print("\t2. Register")
    choice = int(input("\nYour choice : "))
    if choice == 1:
        print("login")
        #if login correct => go to menu
        menu()
    elif choice ==2:
        print("register")
        #after registration => go to login
    else:
        getout()



if __name__ == '__main__':
    main()