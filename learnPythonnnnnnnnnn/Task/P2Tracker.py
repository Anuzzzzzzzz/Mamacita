import csv

students = {}  # store multiple students

while True:
    print("\n--- STUDENT SCORE TRACKER ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Export CSV")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        # Add a student
        name = input("Enter student name: ")
        math = float(input("Math score: "))
        english = float(input("English score: "))
        science = float(input("Science score: "))

        students[name] = {
            "Math": math,
            "English": english,
            "Science": science
        }
        print(f"{name} added ✅")

    elif choice == "2":
        # View all students with average and grade
        if not students:
            print("No students found.")
        else:
            for name, scores in students.items():
                avg = sum(scores.values()) / len(scores)
                # Assign grade
                if avg >= 90: grade = "A"
                elif avg >= 80: grade = "B"
                elif avg >= 70: grade = "C"
                elif avg >= 60: grade = "D"
                else: grade = "F"

                print(f"{name} → Avg: {avg:.2f}, Grade: {grade}")

    elif choice == "3":
        # Search for a student
        search_name = input("Enter student name to search: ")
        if search_name in students:
            scores = students[search_name]
            avg = sum(scores.values()) / len(scores)
            if avg >= 90: grade = "A"
            elif avg >= 80: grade = "B"
            elif avg >= 70: grade = "C"
            elif avg >= 60: grade = "D"
            else: grade = "F"
            print(f"{search_name} → Scores: {scores}, Avg: {avg:.2f}, Grade: {grade}")
        else:
            print("Student not found.")

    elif choice == "4":
        # Export to CSV
        with open("students_summary.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Math", "English", "Science", "Average", "Grade"])
            for name, scores in students.items():
                avg = sum(scores.values()) / len(scores)
                if avg >= 90: grade = "A"
                elif avg >= 80: grade = "B"
                elif avg >= 70: grade = "C"
                elif avg >= 60: grade = "D"
                else: grade = "F"
                writer.writerow([name, scores["Math"], scores["English"], scores["Science"], f"{avg:.2f}", grade])
        print("CSV exported as students_summary.csv ✅")

    elif choice == "5":
        print("Bye 👋")
        break

    else:
        print("Invalid choice")
