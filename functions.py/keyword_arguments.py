#I want to print 'Hello Joshua Solar Hernandez'

def hello(first_name, middle, last_name):
    print("Hello", first_name, middle, last_name)
    

#positional arguments

hello("Joshua","Solar","Hernandez")  #the console will print 'Hello Joshua Solar Hernandez'

hello("Solar","Joshua","Hernandez")  #the console will print 'Hello Solar Joshua Hernandez'



#keyword arguments

hello(last_name="Hernandez", first_name="Joshua", middle="Solar")  
                            #the console will print 'Hello Joshua Solar Hernandez'
