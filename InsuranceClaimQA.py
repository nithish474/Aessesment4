from InsuranceClaim import InsuranceClaim

print("===== INSURANCE CLAIM QA =====")

claim = InsuranceClaim()

print("\nTest 1: Valid Claim")

claim.process_claim(
    "POL1001",
    "C101",
    "Health",
    50000,
    200000,
    "2025-01-01",
    "2026-01-10",
    0,
    30,
    "Accident",
    "Available"
)

print("\nTest 2: Invalid Incident Date")

claim.process_claim(
    "POL1002",
    "C102",
    "Health",
    50000,
    200000,
    "2026-06-01",
    "2026-01-01",
    0,
    30,
    "Accident",
    "Available"
)
print("\nTest 3: Excessive Claim")

claim.process_claim(
    "POL1003",
    "C103",
    "Health",
    500000,
    200000,
    "2025-01-01",
    "2026-05-01",
    0,
    35,
    "Accident",
    "Available"
)

print("\nTest 4: Missing Documents")

claim.process_claim(
    "POL1004",
    "C104",
    "Vehicle",
    50000,
    100000,
    "2025-01-01",
    "2026-04-01",
    0,
    40,
    "Accident",
    "Missing"
)
print("\nTest 5: Multiple Previous Claims")

claim.process_claim(
    "POL1005",
    "C105",
    "Health",
    50000,
    100000,
    "2025-01-01",
    "2026-05-01",
    5,
    50,
    "Accident",
    "Available"
)
print("\nTest 6: Fraud Scenario")

claim.process_claim(
    "POL1006",
    "C106",
    "Health",
    500000,
    200000,
    "2026-01-01",
    "2026-01-10",
    5,
    30,
    "Accident",
    "Missing"
)

print("\nTest 7: Invalid Policy Number")

claim.process_claim(
    "INVALID123",
    "C107",
    "Health",
    50000,
    100000,
    "2025-01-01",
    "2026-05-01",
    0,
    30,
    "Accident",
    "Available"
)

print("\n===== QA COMPLETED =====")
