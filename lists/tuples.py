#ordered and it cannot be modified

student = ("Josh", 18, "Male")

print(student.count("Josh"))
print(student.index("Male"))
print(student[1])

for i in student:
    print(i)

if "Josh" in student:
    print("Josh is in here.")