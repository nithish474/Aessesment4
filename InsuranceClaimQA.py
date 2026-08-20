from InsuranceClaim import InsuranceClaim


print("===== INSURANCE CLAIM QA =====")

claim = InsuranceClaim()


# Test 1
print("\nTest 1: Valid Claim")

claim.process_claim(
    "POL1001",
    "C101",
    "Health",
    50000,
    200000,
    "2025-01-01",
    "2026-12-31",
    "2026-01-10",
    0,
    30,
    "Accident",
    "Available"
)


# Test 2
print("\nTest 2: Expired Policy")

claim.process_claim(
    "POL1002",
    "C102",
    "Health",
    50000,
    200000,
    "2025-01-01",
    "2025-12-31",
    "2026-01-10",
    0,
    30,
    "Accident",
    "Available"
)


# Test 3
print("\nTest 3: Claim Before Policy Start")

claim.process_claim(
    "POL1003",
    "C103",
    "Health",
    50000,
    200000,
    "2026-06-01",
    "2026-12-31",
    "2026-01-01",
    0,
    30,
    "Accident",
    "Available"
)


# Test 4
print("\nTest 4: Excessive Claim Amount")

claim.process_claim(
    "POL1004",
    "C104",
    "Health",
    500000,
    200000,
    "2025-01-01",
    "2026-12-31",
    "2026-05-01",
    0,
    35,
    "Accident",
    "Available"
)


# Test 5
print("\nTest 5: Missing Documents")

claim.process_claim(
    "POL1005",
    "C105",
    "Vehicle",
    50000,
    100000,
    "2025-01-01",
    "2026-12-31",
    "2026-04-01",
    0,
    40,
    "Accident",
    "Missing"
)


# Test 6
print("\nTest 6: Multiple Previous Claims")

claim.process_claim(
    "POL1006",
    "C106",
    "Health",
    50000,
    100000,
    "2025-01-01",
    "2026-12-31",
    "2026-05-01",
    5,
    50,
    "Accident",
    "Available"
)


# Test 7
print("\nTest 7: Fraud Scenario")

claim.process_claim(
    "POL1007",
    "C107",
    "Health",
    500000,
    200000,
    "2026-01-01",
    "2026-12-31",
    "2026-01-10",
    5,
    30,
    "Accident",
    "Missing"
)


# Test 8
print("\nTest 8: Boundary Claim Amount")

claim.process_claim(
    "POL1008",
    "C108",
    "Health",
    200000,
    200000,
    "2025-01-01",
    "2026-12-31",
    "2026-05-01",
    0,
    30,
    "Accident",
    "Available"
)


# Test 9
print("\nTest 9: Invalid Policy Number")

claim.process_claim(
    "INVALID123",
    "C109",
    "Health",
    50000,
    100000,
    "2025-01-01",
    "2026-12-31",
    "2026-05-01",
    0,
    30,
    "Accident",
    "Available"
)


# Test 10
print("\nTest 10: Invalid Incident Date")

claim.process_claim(
    "POL1010",
    "C110",
    "Health",
    50000,
    100000,
    "2025-01-01",
    "2026-12-31",
    "invalid-date",
    0,
    30,
    "Accident",
    "Available"
)

print("\n===== QA COMPLETED =====")
