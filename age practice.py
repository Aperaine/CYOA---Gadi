age = int(input("Enter your age:\n"))
isStudent = input("Are you a student? (y/n)\n")

if age < 18:
    print ("Eligible for minor student discount") if isStudent == "y" else print ("Minor but not student, no discount")
elif age <= 60:
    print ("Eligible for student discount ") if isStudent == "y" else print ("Adult but not student, no discount")
else:
    print("Eligible for senior discount")