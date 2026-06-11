class StudentManager:
    def __init__(self):
        self.students = [
            {"roll_no": 101, "name": "Amit", "marks": 85},
            {"roll_no": 102, "name": "nitish", "marks": 90},
            {"roll_no": 103, "name": "nitin", "marks": 78},
            {"roll_no":104,"name":"raghav","marks":88},
            {"roll_no":105,"name":"raga","marks":8},
            {"roll_no":106,"name":"keju_ji","marks":83},
            {"roll_no":107,"name":"modi","marks":2}
        ]

    def add_student(self):
        roll_no = int(input("Enter Roll No: "))

        for student in self.students:
            if student["roll_no"] == roll_no:
                print("Student already exists!")
                return

        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        self.students.append({
            "roll_no": roll_no,
            "name": name,
            "marks": marks
        })

        print("Student added successfully!")

    def search_student(self):
        roll_no = int(input("Enter Roll No to Search: "))

        for student in self.students:
            if student["roll_no"] == roll_no:
                print("\nStudent Found")
                print("Roll No:", student["roll_no"])
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                return

        print("Student not found!")

    def update_student(self):
        roll_no = int(input("Enter Roll No to Update: "))

        for student in self.students:
            if student["roll_no"] == roll_no:
                student["name"] = input("Enter New Name: ")
                student["marks"] = float(input("Enter New Marks: "))
                print("Record updated successfully!")
                return

        print("Student not found!")

    def delete_student(self):
        roll_no = int(input("Enter Roll No to Delete: "))

        for student in self.students:
            if student["roll_no"] == roll_no:
                self.students.remove(student)
                print("Record deleted successfully!")
                return

        print("Student not found!")

    def display_all(self):
        if len(self.students) == 0:
            print("No records found!")
            return

        print("\n----- Student Records -----")

        for student in self.students:
            print("-" * 25)
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Marks   :", student["marks"])


manager = StudentManager()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.search_student()

    elif choice == "3":
        manager.update_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        manager.display_all()

    elif choice == "6":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")