# declare constance for in state and out of state pricing to avoid using magic numbers in the code.
IN_STATE_PRICE = 225
OUT_STATE_PRICE = 820


def calculate_hours_and_bill(student, courses):  # Pass in student object and courses dictionary.
    hours = 0  # start counter to count total hours
    # iterates through each course in course list for the student object, gets the course object,
    # then gets the hours that course is worth and adds it to the total count
    for course in student.courses:
        course = courses[course]
        hours += course.hours
    # returns the hours and cost based on if the student is in state or out of state.
    if student.in_state:
        return hours, hours * IN_STATE_PRICE
    else:
        return hours, hours * OUT_STATE_PRICE


# pass in two integers for hours and cost, it formats them and prints them.
def display_hours_and_bill(hours, cost):
    print(f"Course load: {hours} credit hours")
    print(f"Enrollment cost: ${cost:.2f}")
