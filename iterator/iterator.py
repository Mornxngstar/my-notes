
my_list = [1,2,3,4,5]
my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break


# That is how a for loop works
# for element in my_list:
#     print(element)