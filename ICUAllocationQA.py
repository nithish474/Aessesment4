from ICUAllocation import ICUAllocation

print("===== ICU ALLOCATION QA =====")

icu = ICUAllocation(2)

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
print("\nTest 3: Emergency Patient")
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

print("\nTest 8: Waiting List")
icu.show_waiting()

print("\n===== QA COMPLETED =====")
