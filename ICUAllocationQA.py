from ICUAllocation import ICUAllocation


print("===== ICU ALLOCATION QA =====")

icu = ICUAllocation(2)


# Test 1
print("\nTest 1: Critical Patient")

icu.add_patient(
    "P101",
    75,
    85,
    130,
    170,
    40,
    3
)


# Test 2
print("\nTest 2: Normal Patient")

icu.add_patient(
    "P102",
    25,
    98,
    75,
    120,
    37,
    0
)


# Test 3
print("\nTest 3: Emergency Case")

icu.add_patient(
    "P103",
    40,
    95,
    90,
    120,
    37,
    0,
    emergency=True
)


# Test 4
print("\nTest 4: No ICU Beds")

icu.add_patient(
    "P104",
    60,
    88,
    130,
    170,
    40,
    2
)


# Test 5
print("\nTest 5: Duplicate Patient")

icu.add_patient(
    "P101",
    50,
    95,
    80,
    120,
    37,
    0
)


# Test 6
print("\nTest 6: Invalid Oxygen")

icu.add_patient(
    "P105",
    40,
    150,
    80,
    120,
    37,
    0
)


# Test 7
print("\nTest 7: Invalid Heart Rate")

icu.add_patient(
    "P106",
    40,
    95,
    -10,
    120,
    37,
    0
)


# Test 8
print("\nTest 8: Priority Boundary")

icu.add_patient(
    "P107",
    30,
    93,
    80,
    120,
    37,
    1
)


# Test 9
print("\nTest 9: Multiple Patients Competing")

icu.add_patient(
    "P108",
    80,
    84,
    130,
    180,
    40,
    4
)

icu.show_allocated()

icu.show_waiting()

print("\n===== QA COMPLETED =====")
