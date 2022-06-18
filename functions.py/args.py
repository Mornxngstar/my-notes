 #adding a '*args', will pack the arguments given into a tuple, we can name if as we like, for instance: '*stuff'

def add(*args): 
    sum = 0
    args = list(args)  #If we convert this tuple into a list we'll be able to modify it
    args[0] = 0

    for i in args:
        sum += i
        
    return sum

print(add(1,2,3))