from datetime import datetime
class InsuranceClaim:
    def process_claim(
        self,
        policy_number,
        customer_id,
        policy_type,
        claim_amount,
        coverage,
        policy_start,
        incident_date,
        previous_claims,
        age,
        incident_type,
        documents
    ):
        if not policy_number.startswith("POL"):
            print("Invalid policy number")
            return
        start = datetime.strptime(
            policy_start,
            "%Y-%m-%d"
        )
        incident = datetime.strptime(
            incident_date,
            "%Y-%m-%d"
        )
        if incident < start:
            print("Claim rejected: Incident before policy start")
            return
        fraud_score = 0
        days_after_policy = (incident - start).days
        if previous_claims >= 3:
            fraud_score += 3
        if claim_amount > coverage:
            fraud_score += 3
        if days_after_policy <= 30:
            fraud_score += 3
        if documents == "Missing":
            fraud_score += 3
        if claim_amount <= 0:
            print("Invalid claim amount")
            return
        deductible = coverage * 0.05
        maximum_payable = coverage - deductible
        payout = min(
            claim_amount,
            maximum_payable
        )
        customer_contribution = claim_amount - payout
        if fraud_score >= 8:
            status = "FRAUD SUSPECTED"
        elif fraud_score >= 5:
            status = "MANUAL REVIEW"
        elif claim_amount > coverage:
            status = "REJECTED"
        else:
            status = "APPROVED"
        print("Policy Number:", policy_number)
        print("Customer ID:", customer_id)
        print("Policy Type:", policy_type)
        print("Incident Type:", incident_type)
        print("\nMaximum Payable:", maximum_payable)
        print("Deductible:", deductible)
        print(
            "Customer Contribution:",
            customer_contribution
        )
        print("Insurance Payout:", payout)
        print("Fraud Risk Score:", fraud_score)
        print("Claim Status:", status)
claim = InsuranceClaim()
claim.process_claim(
    policy_number="POL12345",
    customer_id="C101",
    policy_type="Health",
    claim_amount=150000,
    coverage=200000,
    policy_start="2026-01-01",
    incident_date="2026-06-15",
    previous_claims=1,
    age=30,
    incident_type="Accident",
    documents="Available"
)
