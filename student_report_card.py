"""
Student Report Card Generator

Design a system that:
- Accepts student marks for multiple subjects
- Calculates average and assigns grades
- Displays a final report card

Use classes and modular code structure.
"""


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}  # subject: marks

    def add_mark(self, subject, mark):
        if 0 <= mark <= 100:
            self.marks[subject] = mark
        else:
            raise ValueError("Mark should be between 0 and 100.")

    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def assign_grade(self):
        average = self.calculate_average()
        if average >= 90:
            return 'A+'
        elif average >= 80:
            return 'A'
        elif average >= 70:
            return 'B'
        elif average >= 60:
            return 'C'
        elif average >= 50:
            return 'D'
        else:
            return 'F'

    def generate_report_card(self):
        print("------ Report Card ------")
        print(f"Student Name: {self.name}")
        print("Subjects and Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        average = self.calculate_average()
        grade = self.assign_grade()
        print(f"\nAverage Marks: {average:.2f}")
        print(f"Grade: {grade}")
        print("-------------------------")


# Example usage
def main():
    student = Student(input("Enter student name: "))
    
    num_subjects = int(input("Enter number of subjects: "))
    for _ in range(num_subjects):
        subject = input("Enter subject name: ")
        mark = float(input(f"Enter marks for {subject}: "))
        student.add_mark(subject, mark)

    student.generate_report_card()


if __name__ == "__main__":
    main()
