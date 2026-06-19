students = []


def add_student():
    try:
        roll = input("Enter Roll Number: ")

        # Check for duplicate roll number
        for student in students:
            if student[0] == roll:
                print("Roll Number already exists!")
                return

        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100.")
            return

        students.append([roll, name, marks])

        print("Student added successfully!")

    except ValueError:
        print("Invalid Marks! Please enter a numeric value.")

    except Exception as e:
        print("Unexpected Error:", e)


def view_students():
    try:
        if len(students) == 0:
            print("No students found.")
            return

        print("\n===== Student Records =====")
        print("Roll No\t\tName\t\tMarks")

        for student in students:
            print(f"{student[0]}\t\t{student[1]}\t\t{student[2]}")

    except Exception as e:
        print("Unexpected Error:", e)


def search_student():
    try:
        roll = input("Enter Roll Number to Search: ")

        for student in students:
            if student[0] == roll:
                print("\n===== Student Found =====")
                print("Roll No :", student[0])
                print("Name    :", student[1])
                print("Marks   :", student[2])
                return

        print("Student not found.")

    except Exception as e:
        print("Unexpected Error:", e)


def update_student():
    try:
        roll = input("Enter Roll Number to Update: ")

        for student in students:
            if student[0] == roll:

                student[1] = input("Enter New Name: ")

                marks = float(input("Enter New Marks: "))

                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100.")
                    return

                student[2] = marks

                print("Record updated successfully!")
                return

        print("Student not found.")

    except ValueError:
        print("Invalid Marks! Please enter a numeric value.")

    except Exception as e:
        print("Unexpected Error:", e)


def delete_student():
    try:
        roll = input("Enter Roll Number to Delete: ")

        for student in students:
            if student[0] == roll:
                students.remove(student)
                print("Record deleted successfully!")
                return

        print("Student not found.")

    except Exception as e:
        print("Unexpected Error:", e)


# Main Program
while True:
    try:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("Exiting Program...")
            break

        else:
            print("Please enter a number between 1 and 6.")

    except ValueError:
        print("Invalid Input! Please enter a valid number.")

    except Exception as e:
        print("Unexpected Error:", e)