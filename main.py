# ================================
# School Management System
# ================================

students = []

while True:
    print("\n====== MENU ======")
    print("1. Add new student")
    print("2. Show all studentds")
    print("3. Write an evaluation")
    print("4. Student`s age identificator")
    print("5. Calculating semester grades")
    print("6. THE END ||| EXIT")
    print("=======================================")

    choice = input("Choose option: ")

    # ---------- 1. ახალი მოსწავლის დამატება ----------
    if choice == "1":
        name = input("Enter name:: ").strip().capitalize()
        surname = input("Enter surname: ").strip().capitalize()
        age_input = int(input("Enter age: "))

        age = int(age_input)

        exists = False
        for student in students:
            if student[0] == name and student[1] == surname:
                exists = True

        if exists:
            print("❌ This student it was added!")
        else:
            students.append([name, surname, age, []])
            print("✅ Student added sucessful!")

    # ---------- 2. ყველა მოსწავლის ნახვა ----------
    elif choice == "2":
        if len(students) == 0:
            print("⚠️ System is empty!")
        else:
            number = 1
            for student in students:
                print("-" * 30)
                print(str(number) + ".", student[0], student[1])
                print("Age:", student[2])

                if student[2] < 13:
                    print("Status: Chils")
                elif student[2] < 18:
                    print("Status:  Teenager")
                else:
                    print("Status: Adult")

                if len(student[3]) == 0:
                    print("Evaluations: doesn't have!")
                else:
                    print("Evaluations:", student[3])

                number += 1

    # ---------- 3. შეფასებების დამატება ----------
    elif choice == "3":
        if len(students) == 0:
            print("⚠️ No students have been added yet.")
            continue

        name = input("Enter name: ").strip().capitalize()
        surname = input("Enter surname: ").strip().capitalize()

        found = False
        for student in students:
            if student[0] == name and student[1] == surname:
                found = True

                while True:
                    grade_input = input("Enter evaluation (q or ქ - Exit): ").strip()

                    if grade_input.lower() == "q" or grade_input == "ქ":
                        break

                    if grade_input.isdigit():
                        student[3].append(int(grade_input))
                        print("✅ Evaluation added successfully")
                    else:
                        print("❌ Evaluation must be a number!")

                break

        if not found:
            print("❌ Student not found")
    # ---------- 4. სტატუსის განსაზღვრა ----------
    elif choice == "4":
        name = input("Enter name: ").strip().capitalize()
        surname = input("Enter surname: ").strip().capitalize()

        found = False
        for student in students:
            if student[0] == name and student[1] == surname:
                found = True

                if student[2] < 13:
                    print("Status: Child")
                elif student[2] < 18:
                    print("Status: Teenager")
                else:
                    print("Status: Adult")
                break

        if not found:
            print("❌ Student not found")

    # ---------- 5. წლიური შეფასების გამოთვლა ----------
    elif choice == "5":
        name = input("Enter name: ").strip().capitalize()
        surname = input("Enter surname: ").strip().capitalize()

        found = False
        for student in students:
            if student[0] == name and student[1] == surname:
                found = True

                if len(student[3]) == 0:
                    print("⚠️ Student has not got evaluations!!!")
                    break

                total = 0
                count = 0

                for grade in student[3]:
                    total += grade
                    count += 1

                average = total / count

                # დამრგვალება
                integer_part = int(average)
                decimal_part = average - integer_part

                if decimal_part >= 0.5:
                    final_grade = integer_part + 1
                else:
                    final_grade = integer_part

                print("Annual score:", final_grade)
                break

        if not found:
            print("❌  Student not found")

    # ---------- 6. გამოსვლა ----------
    elif choice == "6":
        print("👋 Program is shutting down!!! Good bye!!!")
        break

    else:
        print("❌ Incorrect option!!!")
