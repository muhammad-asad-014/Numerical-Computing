import math
def func(x):
    return (x)*(math.sin(x))+(x**3)-11 # write your eq here

def mid(a,b):
    return (a+b)/2

def error(y,x):
    return abs(y-x)

def bisection(a,b,i):
    from prettytable import PrettyTable # install this
    table = PrettyTable()
    table.field_names = ["Iteration #", "a", "c","b", "f(a)","f(b)","f(c)","error"]
    x = 0
    c0 = 0
    for i in range(i):
        x+=1
        fa = func(a)
        fb = func(b)
        c = mid(a,b)
        fc = func(c)
        table.add_row([x,a,c,b,fa,fb,fc,error(c,c0)])
        if fc==0:
            break
        elif (fa*fc)<0:
            b = c
        elif (fb*fc)<0:
            a = c
        c0=c
    print(table)

p1 = float(input("Enter the value of a: "))
p2 = float(input("Enter the value of b: "))
iterations = int(input("Enter number of Iterations: "))
bisection(p1,p2, iterations)
