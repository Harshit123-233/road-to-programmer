"""Phase 02: OOP
Day: 19th
Part: 06
Topics Learned Today:-
1. Instance Method
2. @staticmethod
3. @classmethod"""

class Student:

    # Class attribute (shared by all students)
    school_name = "Konoha High School"

    def __init__(self, name, marks, roll_number):
        self.name = name
        self.marks = marks
        self.roll_number = roll_number

    @staticmethod
    def is_valid_marks(marks):  # Static method - doesn't need self or cls
        """Check if marks are within valid range. 
        No access to instance or class data."""
        return 0 <= marks <= 100

    def update_marks(self, marks):  # Instance method
        """Instance method - works with specific student's data."""
        if self.is_valid_marks(marks):
            self.marks = marks
            print(f"Marks updated successfully for {self.name}")
        else:
            print("Invalid Marks! Must be between 0 and 100.")

    @classmethod
    def from_dict(cls, data):  # Class method
        """Alternative constructor using classmethod.
        Useful when creating object from dictionary."""
        return cls(
            data["name"],
            data["marks"],
            data["roll_number"]
        )

    def is_promoted(self):
        """Returns promotion status or None if marks are invalid."""
        if not self.is_valid_marks(self.marks):
            return None   # None means invalid marks
        
        if self.marks >= 33:
            return "is promoted"
        else:
            return "isn't promoted"

    def __str__(self):
        status = self.is_promoted()
        
        if status is None:
            return f"{self.name} (Roll No: {self.roll_number}) has invalid marks: {self.marks}."
        
        return f"{self.name} (Roll No: {self.roll_number}) has scored {self.marks} and hence {status}."


# ==================== TESTING ====================

if __name__ == "__main__":
    naruto = Student("Naruto", 150, 21)
    luffy = Student("Luffy", 98, 22)

    print(naruto)
    print(luffy)

    # Demonstrating update_marks
    print("\n--- Updating Marks ---")
    naruto.update_marks(85)   # Should work
    print(naruto)

    luffy.update_marks(120)   # Should show invalid

    # Using classmethod
    print("\n--- Creating from Dictionary ---")
    data = {"name": "Zoro", "marks": 92, "roll_number": 23}
    zoro = Student.from_dict(data)
    print(zoro)