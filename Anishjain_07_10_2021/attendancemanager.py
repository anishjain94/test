class AttendanceManager:
    def __init__(self, standard):
        self.standard = standard

    def add_attendance(self, date, roll_no, is_present):
        if self.standard.attendance.get(date, None) is None:
            self.standard.attendance[date] = [{roll_no: is_present}]
        else:
            self.standard.attendance[date].append({roll_no: is_present})

    def get_attendance_for_given_date(self, date):
        return self.standard.attendance[date]

    def get_attendance_for_given_student(self, roll_no):
        count = 0
        for date, attendace in self.standard.attendance.items():
            for items in attendace:
                was_present = items.get(roll_no, 0)
                count += int(was_present)

        return count

    def get_attendance_for_given_student_and_date(self, roll_no, date):
        for items in self.standard.attendance[date]:
            was_present = items.get(roll_no, 0)
            return was_present


    def get_attendance(self):
        return self.standard.attendance