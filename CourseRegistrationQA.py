from CourseRegistration import CourseRegistration

print("===== COURSE REGISTRATION QA =====")

c = CourseRegistration()

print("\nTest 1: Valid Registration")

completed = [
    "Programming",
    "Data Structures",
    "Statistics",
    "Networking"
]

c.register(
    "ST101",
    completed,
    ["DBMS", "AI"],
    10
)

print("\nTest 2: Missing Prerequisite")

c.register(
    "ST102",
    [],
    ["DBMS"],
    10
)

print("\nTest 3: Credit Limit Violation")

c.register(
    "ST103",
    completed,
    ["DBMS", "AI", "ML"],
    5
)


print("\nTest 4: Timetable Conflict")

c.register(
    "ST104",
    completed,
    ["DBMS", "ML"],
    10
)
print("\nTest 5: Duplicate Registration")

c.register(
    "ST101",
    completed,
    ["DBMS"],
    10
)

print("\nTest 6: Invalid Course")

c.register(
    "ST105",
    completed,
    ["Python"],
    10
)

print("\nTest 7: Boundary Credit")

c.register(
    "ST106",
    completed,
    ["DBMS", "AI"],
    8
)

print("\n===== QA COMPLETED =====")
