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
        policy_end,
        incident_date,
        previous_claims,
        age,
        incident_type,
        documents
    ):

        if not policy_number.startswith("POL"):

            print("Invalid policy number")

            return

        if claim_amount <= 0:

            print("Invalid claim amount")

            return

        try:

            start = datetime.strptime(
                policy_start,
                "%Y-%m-%d"
            )

            end = datetime.strptime(
                policy_end,
                "%Y-%m-%d"
            )

            incident = datetime.strptime(
                incident_date,
                "%Y-%m-%d"
            )

        except ValueError:

            print("Invalid incident date")

            return

        if end < start:

            print("Invalid policy dates")

            return

        if incident < start:

            print(
                "Claim rejected: Incident before policy start"
            )

            return

        if incident > end:

            print(
                "Claim rejected: Policy expired"
            )

            return

        fraud_score = 0

        days_after_policy = (
            incident - start
        ).days

        if previous_claims >= 3:

            fraud_score += 3

        if claim_amount > coverage:

            fraud_score += 3

        if days_after_policy <= 30:

            fraud_score += 3

        if documents == "Missing":

            fraud_score += 3

        deductible = coverage * 0.05

        maximum_payable = coverage - deductible

        payout = min(
            claim_amount,
            maximum_payable
        )

        customer_contribution = max(
            0,
            claim_amount - payout
        )

        if fraud_score >= 8:

            status = "FRAUD SUSPECTED"

        elif fraud_score >= 5:

            status = "MANUAL REVIEW"

        elif claim_amount > coverage:

            status = "REJECTED"

        else:

            status = "APPROVED"

        print("\nPolicy Number:", policy_number)

        print("Customer ID:", customer_id)

        print("Policy Type:", policy_type)

        print("Customer Age:", age)

        print("Incident Type:", incident_type)

        print(
            "Maximum Payable:",
            maximum_payable
        )

        print(
            "Deductible:",
            deductible
        )

        print(
            "Customer Contribution:",
            customer_contribution
        )

        print(
            "Insurance Payout:",
            payout
        )

        print(
            "Fraud Risk Score:",
            fraud_score
        )

        print(
            "Claim Status:",
            status
        )

        return status


if __name__ == "__main__":

    claim = InsuranceClaim()

    claim.process_claim(
        policy_number="POL12345",
        customer_id="C101",
        policy_type="Health",
        claim_amount=150000,
        coverage=200000,
        policy_start="2026-01-01",
        policy_end="2026-12-31",
        incident_date="2026-06-15",
        previous_claims=1,
        age=30,
        incident_type="Accident",
        documents="Available"
    )
