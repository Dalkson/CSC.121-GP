from billing import display_hours_and_bill, calculate_hours_and_bill
from classes import Student, Course
from student import add_course, drop_course, list_courses


def login(students):
    while True:
        student_id = input("Enter ID to log in, or 0 to quit: ")
        if student_id == "0":
            exit()
        try:
            student = students[student_id]
        except KeyError:
            print("Student not found. Please try again.")
            continue
        pin = input("Enter PIN: ")
        if pin != student.pin:
            print("ID or PIN incorrect")
            continue
        print("ID and PIN verified")
        return student


def main():
    # initializes dictionaries and fills with data.
    # Student('ID', PIN, (In state True or False), list of classes)
    students = {'1001': Student('1001', '111', True, ['CSC102']), '1002': Student('1002', '222', False, ['CSC103']),
                '1003': Student('1003', '333', True, ['CSC101']), '1004': Student('1004', '444', False, ['CSC101'])}

    # Course('Name', credit hours, max size, list of students)
    courses = {'CSC101': Course('CSC101', 3, 3, ['1004', '1003']), 'CSC102': Course('CSC102', 4, 2, ['1001']),
               'CSC103': Course('CSC103', 5, 1, ['1002']), 'CSC104': Course('CSC104', 3, 3, [])}

    # main loop
    while True:
        student = login(students)
        while True:
            choice = input("1. Add course\n2. Drop course\n3. List course\n4. Display bill\n5. Quit\n Choice: ")
            match choice:
                case '1':
                    add_course(student, courses)
                case '2':
                    drop_course(student, courses)
                case '3':
                    list_courses(student)
                case '4':
                    hours, cost = calculate_hours_and_bill(student, courses)
                    display_hours_and_bill(hours, cost)
                case '5':
                    break
                case _:
                    print('Invalid choice, please try again.')
            print()


main()
