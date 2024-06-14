import csv

# Read the CSV file
with open('marks.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

# 1. Average marks of students in Maths
total_math_marks = sum(int(row['Marks_Maths']) for row in data)
average_math_marks = total_math_marks / len(data)
print(f"Ans1: Average Marks in Maths is: {average_math_marks:.0f}")

# 2. Average marks of the class 5 in English
class_5_english_marks = [int(row['Marks_English']) for row in data if row['Class'] == '5']
if class_5_english_marks:
    average_class_5_english_marks = sum(class_5_english_marks) / len(class_5_english_marks)
    print(f"Ans2: Average marks of the class 5 in English: {average_class_5_english_marks:.0f}")
else:
    print("Ans2: No students found in class 5")

# 3. Find the count of students which failed (passing marks is 40)
failed_students = sum(1 for row in data
                      if int(row['Marks_Maths']) < 40 or int(row['Marks_English']) < 40)
print(f"Ans3: Count of students which failed: {failed_students}")

# 4. List the top 5 scorers, sorted in descending order with marks
students = [(row['Name'], int(row['Marks_Maths']) + int(row['Marks_English'])) for row in data]
students.sort(key=lambda x: x[1], reverse=True)

print("Ans4: List of top 5 scorers")
print("Name | Total Marks")
for i, (name, marks) in enumerate(students[:5], start=1):
    print(f"{i} {name} | {marks}")
