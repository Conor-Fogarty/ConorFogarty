# Imports dictionary containing student core data
import studentfile

# This function is used to retrieve student core data for editing
def pull_student_data(student_id):
    if student_id in studentfile.students:
        return studentfile.students[student_id]
    else:
        return None

def main_read(student_id):
    if __name__ == "__main__":
    # Allows users to input student ID
        student_id = int(input("Enter the student ID: "))

    # Retrieving student core data
    student_data = pull_student_data(student_id)

    if student_data:
        # Prints the student data for admin to observe 
        print("Student ID:", student_id)
        print("Name:", student_data["Name"])
        print("Grade:", student_data["Grade"])
        print("Major:", student_data["Major"])
        print("GPA:", student_data["GPA"])
        print("Home State:", student_data["Home_state"])
    else:
        print("Student ID not found.")
#Prompt for user to interact with
if __name__ == "__main__":
    user_input = input("Would you like to view this students core data? (yes/no): ")
    if user_input.lower() == "yes":
        main_read()
    else:
        print("No student data avaliable")
