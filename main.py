# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from menuopt import addEmploye, seeEmployes, delEmployes, salaryCal







print("--- Human Resource Information System ---")

menu: str = ("\nSelect an option (1 - 5):\n"
             "1: Add employee\n"
             "2: Display saved employees\n"
             "3: Delete saved employee\n"
             "4: Salary calculator\n"
             "5: Exit"
             )

while True:
    try:
        print(menu)
        usr = int(input("\nOption (number + press enter): "))

        if usr == 1:
            addEmploye()
            continue

        elif usr == 2:
            seeEmployes()
            continue

        elif usr == 3:
            delEmployes()
            continue

        elif usr == 4:
            salaryCal()
            continue

        elif usr == 5:
            exit()

        else:
            raise ValueError("Nonexistent menu option")

    except Exception as ex:
        print("-> Please enter a valid option:", str(ex))
        continue

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
