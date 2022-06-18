counts = dict()

names = ["csev","cwen","csev","zqian","cwen"]

# for i in names:
#     if i not in counts:
#         counts[i] = 1
#     else:
#         counts[i] = counts[i] + 1

# print(counts)

for i in names:
    counts[i] = counts.get(i, 0) + 1

print(counts)

