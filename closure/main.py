
def make_multiply(x):

    def multiply(n):
        return x * n
    
    return multiply

times10 = make_multiply(10)
times4 = make_multiply(4)

print(times10(3))
print(times4(5))