import studentIDsCourse
# reads and enters student information into the files and underlying functions
def pull_data(student_id):
    if student_id in studentIDsCourse.students:
        return studentIDsCourse.students[student_id]
    else:
        return None
#prints current information, allows editing via admin 
def edit_student_course(student_id):
    students = studentIDsCourse.students
    student_data = students.get(student_id)
    for id in student_data:
        if student_data:
            print("Past and Current Courses for", student_id)
            print('Course: ', student_data['Course'])
            print('\nEnter the new courses:')
            courses = str(input("Course:"))
        

            # Updating the student data within this file, when adding new courses all previous courses get overriden 
            student_data["Course"] = courses

            # Writing the updated data to studentIDsCourse.py
            with open("studentIDsCourse.py", "w") as file:
                file.write("students = " + str(studentIDsCourse.students))

            print("\nStudent courses have been updated")
        else:
            print("This ID does not correspond to a student in the system")
#Prompt for user to interact with in order to edit student's course list
if __name__ == "__main__":
    student_id = int(input("Enter the student ID: "))

    edit_course_option = input("Do you want to edit the student data? (yes/no): ")
    if edit_course_option.lower() == "yes":
        edit_student_course(student_id)
