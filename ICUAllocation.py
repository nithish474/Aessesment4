class ICUAllocation:

    def __init__(self, beds):

        self.total_beds = beds

        self.available_beds = beds

        self.patients = {}

        self.allocated = []

        self.waiting_list = []

    def calculate_priority(
        self,
        age,
        oxygen,
        heart_rate,
        bp,
        temperature,
        conditions
    ):

        score = 0

        if age >= 65:
            score += 1

        if oxygen < 90:
            score += 4

        elif oxygen < 94:
            score += 2

        if heart_rate < 50 or heart_rate > 120:
            score += 3

        if bp < 90 or bp > 160:
            score += 2

        if temperature > 39 or temperature < 35:
            score += 2

        score += conditions

        return score

    def classify(self, score):

        if score >= 8:
            return "CRITICAL"

        elif score >= 5:
            return "HIGH"

        elif score >= 3:
            return "MEDIUM"

        else:
            return "LOW"

    def priority_value(self, priority):

        values = {
            "CRITICAL": 4,
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1
        }

        return values[priority]

    def add_patient(
        self,
        patient_id,
        age,
        oxygen,
        heart_rate,
        bp,
        temperature,
        conditions,
        emergency=False
    ):

        if patient_id in self.patients:

            print("Duplicate patient ID")

            return False

        if oxygen < 0 or oxygen > 100:

            print("Invalid oxygen level")

            return False

        if heart_rate <= 0:

            print("Invalid heart rate")

            return False

        score = self.calculate_priority(
            age,
            oxygen,
            heart_rate,
            bp,
            temperature,
            conditions
        )

        priority = self.classify(score)

        if emergency:

            priority = "CRITICAL"

            score = 100

        patient = {
            "id": patient_id,
            "score": score,
            "priority": priority,
            "emergency": emergency
        }

        self.patients[patient_id] = patient

        self.waiting_list.append(patient)

        self.allocate_beds()

        return True

    def allocate_beds(self):

        self.waiting_list.sort(
            key=lambda x: (
                x["emergency"],
                self.priority_value(x["priority"]),
                x["score"]
            ),
            reverse=True
        )

        while (
            self.available_beds > 0
            and len(self.waiting_list) > 0
        ):

            patient = self.waiting_list.pop(0)

            self.allocated.append(patient)

            self.available_beds -= 1

            print(
                patient["id"],
                "allocated ICU bed"
            )

            print(
                "Priority:",
                patient["priority"]
            )

    def release_bed(self, patient_id):

        for patient in self.allocated:

            if patient["id"] == patient_id:

                self.allocated.remove(patient)

                self.available_beds += 1

                print(
                    "Bed released from",
                    patient_id
                )

                self.allocate_beds()

                return

        print("Patient not found")

    def show_waiting(self):

        print("\nWaiting List:")

        for patient in self.waiting_list:

            print(
                patient["id"],
                patient["priority"],
                patient["score"]
            )

    def show_allocated(self):

        print("\nAllocated Patients:")

        for patient in self.allocated:

            print(
                patient["id"],
                patient["priority"]
            )


if __name__ == "__main__":

    icu = ICUAllocation(2)

    icu.add_patient(
        "P101",
        70,
        85,
        130,
        170,
        40,
        2
    )

    icu.add_patient(
        "P102",
        30,
        97,
        80,
        120,
        37,
        0
    )

    icu.add_patient(
        "P103",
        65,
        88,
        125,
        80,
        39,
        1,
        emergency=True
    )

    icu.show_allocated()

    icu.show_waiting()

    print(
        "\nAvailable Beds:",
        icu.available_beds
    )
