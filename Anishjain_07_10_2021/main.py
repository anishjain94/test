from datetime import datetime

from attendancemanager import AttendanceManager
from school import School
from standard import Standard
from student import Student


def get_dummy_students():
    dummy_list = list()
    dummy_list.append(Student("anish", "jain", 1))
    dummy_list.append(Student("apurve", "jain", 2))
    dummy_list.append(Student("sonal", "jain", 3))
    dummy_list.append(Student("palak", "jain", 4))
    return dummy_list


def main():
    curr_date = datetime.now().strftime("%Y-%m-%d")
    students = get_dummy_students()
    school = School()

    while True:
        print("\n")
        print("1: Add Standard in School \n")
        print("2: Take Attendence of Students \n")
        print("4: Find Attendence of a particular day \n")
        print("5: Find Attendence of a particular Student \n")
        print("6: Find Attendence of a particular Student by day \n")
        print("7: Get All Attendence of a Standard\n")
        print("8: Change Standard \n")

        print("0: Exit \n")
        print("Enter your option: ")
        choice = int(input())

        if choice == 1:
            school_standard = input("Please Enter Standard ")
            standard = Standard(school_standard, students)
            school.add_standard(standard)

        if choice == 2:
            standard = input("Please Enter Standard of Student: ")
            current_standard = school.get_standard(standard)
            attendance_manager = AttendanceManager(current_standard)

            for student in current_standard.students:
                is_present = input(
                    f"Is {student.first_name} {student.last_name} : {student.roll_no} present today?(y/n) "
                )
                if is_present == "y":
                    attendance_manager.add_attendance(curr_date, student.roll_no, True)
                else:
                    attendance_manager.add_attendance(curr_date, student.roll_no, False)

            attendance_manager.get_attendance()

        elif choice == 4:
            date = input("Enter the date: ")
            print(attendance_manager.get_attendance_for_given_date(date))

        elif choice == 5:
            roll_no = int(input("Enter the roll number of student: "))
            print(attendance_manager.get_attendance_for_given_student(roll_no))

        elif choice == 6:
            roll_no = int(input("Enter the roll no of student: "))
            date = input("Enter the date Format (YYYY-MM-DD)(2021-01-01): ")
            print(
                attendance_manager.get_attendance_for_given_student_and_date(
                    roll_no, date
                )
            )

        elif choice == 7 or choice == 8:
            try:
                standard = input("Please Enter Standard: ")
                current_standard = school.get_standard(standard)
                attendance_manager = AttendanceManager(current_standard)
                print(attendance_manager.get_attendance())
            except KeyError as e:
                print("No Existing Standard Found, Please Try Again")

        elif choice == 0:
            print("Exiting Program")
            exit()

        else:
            print("Please select a valid choice")


if __name__ == "__main__":
    main()