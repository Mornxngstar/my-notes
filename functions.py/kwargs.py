#**kwargs will pack the arguments given into a dictionary

def hello(**kwargs):
    #print("Hello " + kwargs["firstname"], kwargs["lastname"])
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ") 

hello(title="Mr.", firstname="Joshua",middle="Solar", lastname= "Hernandez")