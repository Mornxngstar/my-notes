#changeable, unordered collection of unique key:value pairs
#fast because they use hashing, allow us to access a value quickly

capitals = {"USA":"Washington DC",
            "India":"New Dehli",
            "China":"Beijin",
            "Russia":"Moscow"}

# print(capitals["China"])
print(capitals.get("India"))
# print(capitals.keys())
# print(capitals.values())
print(capitals.items())
capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
# capitals.pop("Russia")
# capitals.clear()

for key,value in capitals.items():
    print(value)