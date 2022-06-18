
students = ["Squidward","Sandy","Patrick","Spongebob","Mr. Krabs"]


#.SORT() METHOD ONLY WORKS WITH LISTS

students.sort()                      # It will sort the values of a list alphabetically
students.sort(reverse=True)          # It will sort the values of a list alphabetically but in reverse

for i in students:
    print(i)


#SORTED() FUNCTION WORKS WITH ITERABLES AS TUPLES, LISTS OR DICTIONARIES

students = ("Squidward","Sandy","Patrick","Spongebob","Mr. Krabs")
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)

#-------------------------------------------------------------------------------------

students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78)]

age = lambda ages : ages[2]

students.sort(key=age)

for i in students:
    print(i)

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

sorted_students = sorted(students)
for i in sorted_students:
    print(i)
