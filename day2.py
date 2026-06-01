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
