import studentfile
import readfile
import editfile
import EditCourses
#start of user prompt, giving them a menu to select from
while True:
    print("\n--- Student Core Data and Student Courses Menu ---")
    print("1. Read Student Core Data")
    print("2. Edit Student Core Data")
    print("3. Edit Student Courses")
    print("4. Exit Program")
    #allows for user input to interact with program, options: read core data, edit core data, edit course data, quit
    user_number = str(input("Enter a number (1-4): "))

#Option 1, read student core data
    if user_number == "1":
        print("\n--- Retrieve Student Data ---")
        student_id = int(input("Enter the student ID: "))

        read_option = input("Do you want to read the student core data? (yes/no): ")
        if read_option.lower() == "yes":
            readfile.main_read(student_id)
#Option 2, edit student core data
    elif user_number == "2":
        print("\n--- Edit Student Core Data ---")
        Access_Code = input('Enter Administrator Access Code: ')
        if Access_Code == '1234':  # Comparing with string '1234'
            student_id = int(input("Enter the student ID: "))

            edit_option = input("Do you want to edit the student core data? (yes/no): ")
            if edit_option.lower() == "yes":
                editfile.edit_student_data(student_id)  
#Options 3, edit course data
    elif user_number == "3":
        print("\n--- Edit Student Courses ---")
        Access_Code = input('Enter Administrator Access Code: ')
        if Access_Code == '1234':  # Comparing with string '1234'
            student_id = int(input("Enter the student ID: "))

            edit_course_option = input("Do you want to edit the student course data? (yes/no): ")
            if edit_course_option.lower() == "yes":
                EditCourses.edit_student_course(student_id)
#Option 4, quit
    elif user_number == "4":
        print('Have a great day!')
        break
