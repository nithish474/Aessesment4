class CourseRegistration:
    def __init__(self):
        self.courses = {
            "DBMS": {
                "credits": 4,
                "prerequisite": "Programming",
                "time": "10-11",
                "capacity": 2,
                "registered": []
            },
            "AI": {
                "credits": 4,
                "prerequisite": "Data Structures",
                "time": "11-12",
                "capacity": 2,
                "registered": []
            },
            "ML": {
                "credits": 3,
                "prerequisite": "Statistics",
                "time": "10-11",
                "capacity": 2,
                "registered": []
            },
            "Cloud": {
                "credits": 3,
                "prerequisite": "Networking",
                "time": "2-3",
                "capacity": 2,
                "registered": []
            }
        }
        self.students = {}
    def register(self, student_id, completed_courses,
                 selected_courses, max_credits):
        if student_id not in self.students:
            self.students[student_id] = []
        total_credits = 0
        timetable = []
        for course in selected_courses:
            if course not in self.courses:
                print("Invalid course:", course)
                continue
            if course in self.students[student_id]:
                print("Duplicate registration:", course)
                continue
            data = self.courses[course]
            prerequisite = data["prerequisite"]
            if prerequisite not in completed_courses:
                print(
                    "Missing prerequisite for",
                    course,
                    ":",
                    prerequisite
                )
                continue
            if data["time"] in timetable:
                print("Timetable conflict for", course)
                continue
            if len(data["registered"]) >= data["capacity"]:
                print(course, "is full")
                continue
            if total_credits + data["credits"] > max_credits:
                print("Credit limit exceeded for", course)
                continue
            self.students[student_id].append(course)
            self.courses[course]["registered"].append(
                student_id
            )
            timetable.append(data["time"])
            total_credits += data["credits"]
            print(course, "registered successfully")
        print(
            "\nTotal Credits for",
            student_id,
            ":",
            total_credits
        )
c = CourseRegistration()
completed = [
    "Programming",
    "Data Structures",
    "Statistics",
    "Networking"
]
selected = [
    "DBMS",
    "AI",
    "ML",
    "Cloud"
]
c.register(
    "24MIS0086",
    completed,
    selected,
    12
)
