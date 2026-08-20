class CourseRegistration:

    def __init__(self):

        self.courses = {

            "DBMS": {
                "credits": 4,
                "prerequisite": "Programming",
                "time": "10-11",
                "capacity": 2,
                "registered": [],
                "semester": 3
            },

            "AI": {
                "credits": 4,
                "prerequisite": "Data Structures",
                "time": "11-12",
                "capacity": 2,
                "registered": [],
                "semester": 4
            },

            "ML": {
                "credits": 3,
                "prerequisite": "Statistics",
                "time": "10-11",
                "capacity": 2,
                "registered": [],
                "semester": 5
            },

            "Cloud": {
                "credits": 3,
                "prerequisite": "Networking",
                "time": "2-3",
                "capacity": 2,
                "registered": [],
                "semester": 4
            }
        }

        self.students = {}

    def register(
        self,
        student_id,
        program,
        semester,
        completed_courses,
        selected_courses,
        max_credits
    ):

        if student_id not in self.students:

            self.students[student_id] = []

        total_credits = 0

        timetable = []

        for course in selected_courses:

            if course not in self.courses:

                print(
                    "Invalid course:",
                    course
                )

                continue

            if course in self.students[student_id]:

                print(
                    "Duplicate registration:",
                    course
                )

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

            if semester < data["semester"]:

                print(
                    "Semester restriction for",
                    course
                )

                continue

            if data["time"] in timetable:

                print(
                    "Timetable conflict for",
                    course
                )

                continue

            if len(data["registered"]) >= data["capacity"]:

                print(
                    course,
                    "is full"
                )

                continue

            if total_credits + data["credits"] > max_credits:

                print(
                    "Credit limit exceeded for",
                    course
                )

                continue

            self.students[student_id].append(course)

            self.courses[course]["registered"].append(
                student_id
            )

            timetable.append(
                data["time"]
            )

            total_credits += data["credits"]

            print(
                course,
                "registered successfully"
            )

        print(
            "\nStudent ID:",
            student_id
        )

        print(
            "Program:",
            program
        )

        print(
            "Semester:",
            semester
        )

        print(
            "Total Credits:",
            total_credits
        )

        return total_credits


if __name__ == "__main__":

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
        "Cloud"
    ]

    c.register(
        "24MIS0086",
        "M.Sc Integrated",
        4,
        completed,
        selected,
        12
    )
