from employee import Employe

def addEmploye():
    while True:
        try:
            nm = input("\nName: ")
            ph = int(input("Phone: "))
            cm = input("Comment: ")

            tmpEm = Employe(nm, ph, cm)
            print(tmpEm.comprobation())

            file = open("data.txt", "a")
            file.write(tmpEm.file())
            file.close()

            input("Press Enter to continue...")

            break

        except Exception as ex:
            print(f"-> Please enter valid data: {ex}")


def seeEmployes():
    file = open("data.txt", "r")
    print(f"\n{file.read()}")
    file.close()

    input("Press Enter to continue...")


def delEmployes():
    seeEmployes()
    delnm = input("Name of employee to  delete (this will delete all employees starting with this input): ")
    file = open("data.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("data.txt", "w")
    for line in lines:
        if line.strip("\n").startswith(delnm):
            continue
        file.write(line)
    file.close()


def salaryCal():
    while True:
        try:
            hourlyWage = float(input("Hourly wage: $"))
            totalHoursWorked = float(input("Total hours worked: "))

            file = open("data.txt", "r")
            numEmp = sum(1 for line in file)
            file.close()
            totalSalary = numEmp * totalHoursWorked * hourlyWage
            print(f"\n{numEmp} employees registered\nTotal salary: ${totalSalary}\n")
            input("Press Enter to continue...")

            break

        except Exception as ex:
            print(f"-> Please enter valid data: {ex}")