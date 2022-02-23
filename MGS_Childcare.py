"""MGS childcare
Created by Francis Torcuato
23/02/2022
"""


def drop_off():
    name = input("What is the name of the child: ")
    child_care_list.append(name)
    print(f"{name} has been added in to MGS childcare")


def pick_up():
    name = input("What is the name of the child: ")
    if name in child_care_list:
        child_care_list.remove(name)
        print(f"{name} has been remove from MGS childcare list")
    else:
        print(f"sorry, we don't have {name} in the list.")


def calc_cost():
    number = int(input("The number of hours: "))
    charge = number * 12
    print(f"The charge for {number} hours is ${charge}")


def print_roll():
    for child in child_care_list:
        print(child)


def quit_programme():
    print("Goodbye")


child_care_list = []
choice = 0


while choice != 5:
    print("-----------------------------------------------------------------------")
    print("Welcome to MGS Childcare")
    print("What would you like to do? Please choose one of the items below")
    print("-----------------------------------------------------------------------")
    print()
    print("1 Drop off a child")
    print("2 Pick up a child")
    print("3 Calculate cost")
    print("4 Print roll")
    print("5 Exit the system")
    print()
    choice=int(input("Enter your choice (number between 1 and 5): "))
    print()

    if choice == 1:
        drop_off()
    elif choice == 2:
        pick_up()
    elif choice == 3:
        calc_cost()
    elif choice == 4:
        print_roll()
    elif choice == 5:
        quit_programme()

