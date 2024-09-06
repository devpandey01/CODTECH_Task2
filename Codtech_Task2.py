class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade
        print(f"Grade added for {subject}")

    def edit_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject] = grade
            print(f"Grade updated for {subject}")
        else:
            print(f"Subject {subject} not found.")

    def delete_grade(self, subject):
        if subject in self.grades:
            del self.grades[subject]
            print(f"Grade deleted for {subject}")
        else:
            print(f"Subject {subject} not found.")

    def display_grades(self):
        if self.grades:
            print("Current Grades:")
            for subject, grade in self.grades.items():
                print(f"{subject}: {grade}")
        else:
            print("No grades available.")

    def calculate_average(self):
        if self.grades:
            average = sum(self.grades.values()) / len(self.grades)
            print(f"Average Grade: {average}")
        else:
            print("No grades to calculate average.")

def menu():
    tracker = StudentGradeTracker()

    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add Grade")
        print("2. Edit Grade")
        print("3. Delete Grade")
        print("4. Display Grades")
        print("5. Calculate Average")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            subject = input("Enter the subject name: ")
            try:
                grade = float(input(f"Enter the grade for {subject}: "))
                tracker.add_grade(subject, grade)
            except ValueError:
                print("Invalid input! Please enter a numeric value for the grade.")

        elif choice == '2':
            subject = input("Enter the subject name to edit: ")
            if subject in tracker.grades:
                try:
                    grade = float(input(f"Enter the new grade for {subject}: "))
                    tracker.edit_grade(subject, grade)
                except ValueError:
                    print("Invalid input! Please enter a numeric value for the grade.")
            else:
                print(f"Subject {subject} not found.")

        elif choice == '3':
            subject = input("Enter the subject name to delete: ")
            tracker.delete_grade(subject)

        elif choice == '4':
            tracker.display_grades()

        elif choice == '5':
            tracker.calculate_average()

        elif choice == '6':
            break

        else:
            print("Invalid choice! Please select a valid option.")

menu()
