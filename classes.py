#
# Group 4
# 4/18/23
# Defines classes that will be used to store data for students and course.
# Only simple classes needed. We modify the data outside the class.
#


class Student:
    def __init__(self, student_id, pin, in_state, courses):
        self.student_id = student_id
        self.pin = pin
        self.in_state = in_state
        self.courses = courses


class Course:
    def __init__(self, name, hours, max_size, roster):
        self.name = name
        self.hours = hours
        self.max_size = max_size
        self.roster = roster
