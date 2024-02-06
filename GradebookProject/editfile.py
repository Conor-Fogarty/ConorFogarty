import studentfile
# Pulls student information into the program
def get_student_data(student_id):
    if student_id in studentfile.students:
        return studentfile.students[student_id]
    else:
        return None
#Core function, prints data for admin to observe before editing, allows editing, then allows admin to enter new that will later be written into dictionary in studentfile.py
def edit_student_data(student_id):
    students = studentfile.students
    student_data = students.get(student_id)
    if student_data:
        print("Current information for student:", student_id)
        print("Name:", student_data["Name"])
        print("Grade:", student_data["Grade"])
        print("Major:", student_data["Major"])
        print("GPA:", student_data["GPA"])
        print("Home State:", student_data["Home_state"])

        print("\nEnter the new information for this student:")
        name = str(input("Name: "))
        grade = str(input("Grade: "))
        assert not grade.lower() == "postgraduate", "Student can not be a Postgraduate"
        major = str(input("Major: "))
        gpa = float(input("GPA: "))
        assert (gpa >= 0) and (gpa <= 4), "Invalid GPA. Please enter a value between 0 and 4."
        home_state = str(input("Home State: "))

        # Updating the student data within this file
        student_data["Name"] = name
        student_data["Grade"] = grade
        student_data["Major"] = major
        student_data["GPA"] = gpa
        student_data["Home_state"] = home_state

        # Writing the updated data to studentfile.py
        with open("studentfile.py", "w") as file:
            file.write("students = " + str(studentfile.students))

        print("\nStudent information has been updated.")
    else:
        print("This ID does not correspond to a student in the system")
#Prompt for user to interact with
if __name__ == "__main__":
    student_id = int(input("Please enter the student's ID: "))

    edit_option = input("Are you sure you want to edit the student core data? (yes/no): ")
    if edit_option.lower() == "yes":
        edit_student_data(student_id)
