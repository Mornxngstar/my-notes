#set = collection is unordered and unindexed. No duplicate values.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")      adds an element
# utensils.update(dishes)     adds more than one element
# utensils.remove("fork")     removes an element only if this exists, else it'll raise an keyerror
# utensils.discard("table")   removes elements and if it does not exists, it returns the original set
# utensils.pop()              removes a random element
# utensils.clear()            removes all the elements

print(utensils | dishes)                       # combines the elements from two sets
# print(dinner_table = utensils.union(dishes))   

print(utensils & dishes)                       # returns the value that both sets have in common 
# print(utensils.intersection(dishes))  

print(utensils - dishes)                       # returns only the values that the first set has and the second doesn't
# print(utensils.difference(dishes))            

print(utensils ^ dishes)                       # returns the values that don't repeat in each of the sets
# print(utensils.symmetric_difference(dishes))        

# for i in dinner_table:
#     print(i)
