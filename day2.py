    # Tuples are similar to lists but are immutable (cannot be changed after creation)

# Tuples cannot be changed after creation
student_record = ("Alice", 20, 85.5, "Computer Science")
print("Student Record Tuple:", student_record)

# Accessing tuple elements
print("Name:", student_record[0])
print("Age:", student_record[1])

# Sets automatically remove duplicates
course_A = {"Alice", "Bob", "Charlie", "Diana"}
course_B = {"Charlie", "Diana", "Eve", "Frank"}

print("Course A students:", course_A)
print("Course B students:", course_B)

# Set operations (Great for finding overlaps)
print("\nStudents in both courses:", course_A & course_B)
print("\nStudents in either courses:", course_A | course_B)
print("\nStudents in only in A:", course_A - course_B)
print("\nStudents in only in B:", course_B & course_A)
print("Only in one course:", course_A ^ course_B)

# Remove duplicates from list using set
scores_with_doplicates = [85, 92, 85, 78, 92, 95, 85]
unique_scores = list(scores_with_doplicates)
print("Unique scores:", unique_scores)

print("\n--- Dictionaries ---")
print("="*50)  
# Dictionaries store key-value pairs and are very useful for structured data
# Dictionaries store data with keys
student = {
    "name": "Alice",
    "age": 20,
    "scores": [85,92, 78],
    "department": "BCA",
    "is_active": True
}

print("Student Dictionary:")
print(student)

# Accessing values
print("\nStudent name:", student['name'])
print("Student scores:", student['scores'])
print("Average scores:", sum(student['scores'])/len(student["scores"]))

# Adding/updating values
student["grade"] = "A"
student["age"] = 21
student["hobbies"] = ["Cording", "Dancaing"]
print("\nAfter update:", student)

alis_scores = student['scores']

alice_passing_scores = [score for score in alis_scores if score >= 80]
print("\n Alice Passing scores (>=80):", alice_passing_scores)

# Conditional statements
# Function to determine grade based on score
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
# Test teh function 
test_scores = [95, 85, 75, 65, 55]
for score in test_scores:
    grade = get_grade(score)
    print("Score:", score, "grade")
    