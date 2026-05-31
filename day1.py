print("Hello, World!")

name = "RAM"
faculty = "Computer Science"
dob = "01/01/2000"
age = 25;

# print("Hello, " +name + "!" + "You are a student of" +faculty + "and your date of birth is "+ dob);
print(f"Hello, {name}!")
print(f"Hello, {name} ! You are a student of {faculty} and your date of birth is {dob}")

#string concatenation
print("Hello, " + name + "!")

# Check data types
print(f"Type of name: {type(name)}")
print(f"Type fo faculty: {type(faculty)}")
print(f"Type fo dob: {type(dob)}")
print(f"Type fo age: {type(age)}")

#multiple assignment
name, faculty, dob, age, is_student, gpa = "Hari", "BCA", "01/01/2000", 25, True, 3.95

#Swap variables easily
x, y = 10, 20
print("Before swap: x=", x, "y=", y)
print("After swap: x=", x, "y=", y)

#Unpack Lists
student_info = ["Charlie", 21, 88.0]
name, age, score = student_info
print("Unpacked:", name, age, score)

name1, *others = student_info
print("Unpacked:", name, age, score)
#try without using others variables

# Creating lists
student_names = ["Alice", "Bob", "Charlie", "Diana"]
student_scores = [85,92,56, 78]

# Accessing elements (indexing starts at 0)
print("\nFirst student:", student_names[0])
print("\nFiLastrst student:", student_names[-1])
print("\nFirst Three:", student_names[0:3])
#all students from index 1 to end
print("Students from index 1 t0 end:", student_names[:])
print("Every second student:", student_names[::2])

#List operations
student_names.append("Eve")   #Add to end
print("\nAfter adding Eve: ", student_names)

student_names.insert(1, "Frank")  # Insert at position
print("After inserting Frank: ", student_names)

student_names.remove("Bob")  # Remove by value
print("After removing: ", student_names)

# List Comprehension (powerful feature!)
passing_scores = [score for score in student_scores if score >= 80]
print("\n Passing scores (>=80):", passing_scores)

# Common methods
print("Number of students: ", len(student_names))
print("Highest score: ", max(student_scores))
print("Lowest score: ", min(student_scores))
