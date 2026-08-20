class ICUAllocation:
    def __init__(self, beds):
        self.available_beds = beds
        self.patients = {}
        self.waiting_list = []
    def calculate_priority(self, age, oxygen, heart_rate,
                           bp, temperature, conditions):
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
    def add_patient(self, patient_id, age, oxygen,
                    heart_rate, bp, temperature,
                    conditions, emergency=False):
        if patient_id in self.patients:
            print("Duplicate patient ID")
            return
        if oxygen < 0 or oxygen > 100:
            print("Invalid oxygen level")
            return
        if heart_rate <= 0:
            print("Invalid heart rate")
            return
        score = self.calculate_priority(
            age, oxygen, heart_rate,
            bp, temperature, conditions
        )
        priority = self.classify(score)
        self.patients[patient_id] = {
            "priority": priority,
            "score": score
        }
        if emergency:
            priority = "CRITICAL"
        if self.available_beds > 0:
            self.available_beds -= 1
            print(patient_id, "allocated ICU bed")
            print("Priority:", priority)
        else:
            self.waiting_list.append(
                (patient_id, priority, score)
            )
            print(patient_id, "added to waiting list")
    def show_waiting(self):
        print("\nWaiting List:")
        priority_order = {
            "CRITICAL": 4,
            "HIGH": 3,
            "MEDIUM": 2,
            "LOW": 1
        }
        self.waiting_list.sort(
            key=lambda x: priority_order[x[1]],
            reverse=True
        )
        for x in self.waiting_list:
            print(x)
icu = ICUAllocation(2)
icu.add_patient(
    "P101", 70, 85,
    130, 170, 40,
    2
)
icu.add_patient(
    "P102", 30, 97,
    80, 120, 37,
    0
)
icu.add_patient(
    "P103", 65, 88,
    125, 80, 39,
    1,
    emergency=True
)
icu.show_waiting()
print("\nAvailable Beds:", icu.available_beds)
