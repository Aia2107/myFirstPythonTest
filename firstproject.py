score = int(input("Enter your score: "))

if score == 90:
    print("Excellent!")
elif score >= 80 or score < 90:
    print("Good!")
elif score <= 70:
    print("Need Improvement!")