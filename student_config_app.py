import os

from dotenv import load_dotenv


load_dotenv()

# TODO 1: Read APP_NAME. Use "Student Config App" as the default value.
app_name = os.getenv("APP_NAME")

# TODO 2: Read TRAINER_NAME. This value is required.
trainer_name = os.getenv("TRAINER_NAME")

# TODO 3: Read BATCH_NAME. Use "Python Essentials" as the default value.
batch_name = os.getenv("BATCH_NAME")

# TODO 4: Read TOTAL_STUDENTS and convert it to an integer.
total_students = os.getenv("TOTAL_STUDENTS")

# TODO 5: Read DEBUG and convert it to a Boolean.
debug = os.getenv("DEBUG")

# TODO 6: Raise a clear error if trainer_name is missing.
if trainer_name is None:
    raise ValueError("trainer name is required")

print(app_name)
print("Trainer:", trainer_name)
print("Batch:", batch_name)
print("Total Students:", total_students)
print("Debug Mode:", debug)

# Challenge:
# Read MAX_ASSIGNMENT_SCORE, calculate 40 percent of it, and print the passing score.
max_assignment_score = int(os.getenv("MAX_ASSIGNMENT_SCORE"))
passing_score = max_assignment_score * 0.4
print(f"passing score is {passing_score}")