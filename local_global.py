# global
pi = 3.14159
def circle(r):
     area_of_circle=pi*r*r  #Accessing global variable here
     result=input(area_of_circle)
circle(4)
#local
def code_base():
    x="I Work At Code Base"
    print(x)
code_base()