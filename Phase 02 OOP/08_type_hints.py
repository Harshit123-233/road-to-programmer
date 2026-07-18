"""Phase 02: OOP
Day: 21st
Part: 08
Topics: Type Hints in Python

What we learned:
- Using type hints for better code readability and IDE support
- Importing from typing module
- Type hints for variables, function parameters, and return types
- Using built-in generics like list[ClassName]
"""

from typing import List  # For older Python versions (< 3.9), list[Student] works in 3.9+


class Student:
    """Represents a student with name, marks, and roll number."""
    
    def __init__(self, name: str, marks: int, roll_number: int) -> None:
        """Initialize a Student instance.
        
        Args:
            name: Student's full name
            marks: Marks obtained (0-100 typically)
            roll_number: Unique roll number
        """
        self.name: str = name
        self.marks: int = marks
        self.roll_number: int = roll_number


# Create student objects
s1 = Student("Naruto", 100, 21)
s2 = Student("Luffy", 98, 22)
s3 = Student("Ichigo", 96, 23)

students: List[Student] = [s1, s2, s3]  # Explicit type hint for the list


def show_topper(student_list: List[Student]) -> str:
    """Find and return the name of the student with highest marks.
    
    Args:
        student_list: List of Student objects
        
    Returns:
        Name of the topper (student with max marks)
        
    """
    if not student_list:
        return "No students in the list"
    
    # Initialize with first student
    topper: Student = student_list[0]
    
    for student in student_list:
        if student.marks > topper.marks:
            topper = student
    
    return topper.name


# Demo
if __name__ == "__main__":
    print("Topper:", show_topper(students))
    print(f"Total students: {len(students)}")
    
    # Example of type hints with Optional and Any
    from typing import Optional, Any
    
    def get_student_info(student: Optional[Student] = None) -> dict[str, Any]:
        """Example function showing Optional and Any."""
        if student is None:
            return {"error": "No student provided"}
        return {
            "name": student.name,
            "marks": student.marks,
            "roll": student.roll_number
        }
    
    print(get_student_info(s1))