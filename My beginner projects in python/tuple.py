# tuple is a collection which is ordered and unchangable (used to group together related data)

student = ("Emo",21,"male")

print(student.count("Emo"))
print(student.index("male"))

for x in student:
    print(x)

if "Emo" in student:
    print("Target is here")