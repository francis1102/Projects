"""Taxi Trips
Created by Francis Torcuato
4/03/2022
"""


# Main function
def main():
    name = ""
    total_value = 0
    fine_list = []

def name_speeder():
    while name != "X":
        print("n\####################")
        name = input("Enter the name of the speeder: ").title()
        if name == "X":
            print_summary(total_value, fine_list)
            break
        else:
            check_warrant(name)
            amount_over = int_check("Enter the amount over the speed limit:")

            fine = int(calc_fine(amount_over))
            total_value + fine
            if fine > 0:
                fine_lists.append({name, amount_over})
            print(f"{name} to be fined ${fine}")

# Summary printed when program ends
def print_summary(total_fines, fine_lists):
    print(f"\n\n******* SUMMARY *****\n\n"
          f"Total fines: {len(fine_lists)}")
    for fine in fine_lists:
        print(f"{fine_lists.index(fine)} + 1")
        print(f"Name: {fine[0]}\tAmount Over Limit: {fine[1]}")
    print(f"Total amount of fines: ${total_fines}")

def calc_fine(amount_over):
    if amount_over < 10:
        fine = 30
    elif amount_over < 15:
        fine = 80
    elif amount_over < 20:
        fine = 120
    elif amount_over < 25:
        fine = 170
    elif amount_over < 30:
        fine = 230
    elif amount_over < 35:
        fine = 300
    elif amount_over < 40:
        fine = 400
    elif amount_over < 45:
        fine = 510
    else:
        fine = 630
    return fine

def int_check(text):
    valid = False
    while not valid:
        try:
            number_to_check = int(input(text))

            if insistance(number_to_check, int):
                valid = True
                return number_to_check

        except ValueError:
            print("Woops...")


def check_warrant (name):
    warrant_list = ["James Wilson", "Helga Norman", "Zachary Conroy"]
    if name in warrant_list:
        print(f"{name} warrant to arrest".upper())


print("*************** Speeding motorists - fines calculator *************** /" "Enter 'X' to exit the program")

main()

