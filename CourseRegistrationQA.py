from CourseRegistration import CourseRegistration


print("===== COURSE REGISTRATION QA =====")

c = CourseRegistration()

completed = [
    "Programming",
    "Data Structures",
    "Statistics",
    "Networking"
]


# Test 1
print("\nTest 1: Valid Registration")

c.register(
    "ST101",
    "M.Sc Integrated",
    5,
    completed,
    ["DBMS", "AI"],
    10
)


# Test 2
print("\nTest 2: Missing Prerequisite")

c.register(
    "ST102",
    "M.Sc Integrated",
    5,
    [],
    ["DBMS"],
    10
)


# Test 3
print("\nTest 3: Credit Limit Violation")

c.register(
    "ST103",
    "M.Sc Integrated",
    5,
    completed,
    ["DBMS", "AI", "ML"],
    5
)


# Test 4
print("\nTest 4: Timetable Conflict")

c.register(
    "ST104",
    "M.Sc Integrated",
    5,
    completed,
    ["DBMS", "ML"],
    10
)


# Test 5
print("\nTest 5: Full Course")

c.register(
    "ST201",
    "M.Sc Integrated",
    5,
    completed,
    ["Cloud"],
    10
)

c.register(
    "ST202",
    "M.Sc Integrated",
    5,
    completed,
    ["Cloud"],
    10
)

c.register(
    "ST203",
    "M.Sc Integrated",
    5,
    completed,
    ["Cloud"],
    10
)


# Test 6
print("\nTest 6: Duplicate Registration")

c.register(
    "ST101",
    "M.Sc Integrated",
    5,
    completed,
    ["DBMS"],
    10
)


# Test 7
print("\nTest 7: Invalid Course")

c.register(
    "ST105",
    "M.Sc Integrated",
    5,
    completed,
    ["Python"],
    10
)


# Test 8
print("\nTest 8: Semester Restriction")

c.register(
    "ST106",
    "M.Sc Integrated",
    2,
    completed,
    ["ML"],
    10
)


# Test 9
print("\nTest 9: Boundary Credit Value")

c.register(
    "ST107",
    "M.Sc Integrated",
    4,
    completed,
    ["DBMS", "AI"],
    8
)

print("\n===== QA COMPLETED =====")
