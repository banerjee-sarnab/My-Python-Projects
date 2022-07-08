# Equations are : 
# a1x+b1y+c1z=d1
# a2x+b2y+c2z=d2
# a3x+b3y+c3z=d3
try :

    a1 = float(input("Enter the value of a1 : "))
    b1 = float(input("Enter the value of b1 : "))
    c1 = float(input("Enter the value of c1 : "))
    d1 = float(input("Enter the value of d1 : "))
    a2 = float(input("Enter the value of a2 : "))
    b2 = float(input("Enter the value of b2 : "))
    c2 = float(input("Enter the value of c2 : "))
    d2 = float(input("Enter the value of d2 : "))
    a3 = float(input("Enter the value of a3 : "))
    b3 = float(input("Enter the value of b3 : "))
    c3 = float(input("Enter the value of c3 : "))
    d3 = float(input("Enter the value of d3 : "))
    x = float(input("Enter initial guess of x :"))
    y = float(input("Enter initial guess of y :"))
    z = float(input("Enter initial guess of z :"))

    n = int(input("Enter number of iterations : "))

    for i in range(n) :
        x = (d1-c1*z-b1*y)/a1
        y = (d2-a2*x-c2*z)/b2
        z = (d3-a3*x-b3*y)/c3

    print(f"The value of x upto {n} iterations is : {x}")
    print(f"The value of y upto {n} iterations is : {y}")
    print(f"The value of z upto {n} iterations is : {z}")

except Exception as e :
    print("Please enter proper values")
