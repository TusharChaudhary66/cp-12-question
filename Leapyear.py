A=int(input("Enter a number"))
if (A%4==0 and A%400==0) or(A%100!=0):
    print("Leap year")
else:
    print("normal year")    