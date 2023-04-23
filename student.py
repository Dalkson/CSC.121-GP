#
# Group 4
# 4/18/23
# Defines 3 functions. These are the main functions for working with courses a student is in.
#

def add_course(student, courses):  # Pass in student object and courses dictionary.
    course_name = input("Enter course you want to add: ")
    # if the course is not in the dictionary, full, or has already been enrolled in by the student,
    # print and error and return.
    if course_name not in courses:
        print("Course not found")
        return
    if course_name in student.courses:
        print("You are already enrolled in that course")
        return
    course = courses[course_name]  # get the course as an object from the dictionary.
    if course.max_size == len(course.roster):
        print("Course already full")
        return
    # add the course name to the student object and add the student ID to the course object.
    student.courses.append(course_name)
    course.roster.append(student.student_id)
    print(f"Course added")


def drop_course(student, courses):  # Pass in student object and courses dictionary.
    course_name = input("Enter course you want to drop: ")
    # if the course is not in the dictionary or is not enrolled in by the student,
    # print and error and return.
    if course_name not in courses:
        print("Course not found")
        return
    if course_name not in student.courses:
        print("You are not enrolled in that course")
        return
    course = courses[course_name]  # get the course as an object from the dictionary.
    # remove the course name from the student object and remove the student ID from the course object.
    student.courses.remove(course_name)
    course.roster.remove(student.student_id)
    print("Course dropped")


def list_courses(student):  # pass in the student object.
    total = 0  # initialize a counter for the total number of courses
    for course in student.courses:  # iterate through each course in the courses list in the student object, then print.
        total += 1
        print(course)
    print(f"Total number: {total}")
