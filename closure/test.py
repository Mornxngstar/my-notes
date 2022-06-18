def make_division_by(x):

    def division(y):
        assert type(x) == int or type(y) == float, "Solo usar numeros"
        return y / x
    
    return division

def run():
    
    divide_by2 = make_division_by(2)
    print(divide_by2(4))

    divide_by5 = make_division_by(5)
    print(divide_by5(10))

if __name__ == '__main__':
    run()
