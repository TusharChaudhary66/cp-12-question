A = float(input("Enter first number: "))
B = float(input("Enter second number: "))
C = float(input("Enter third number: "))
if A+B+C==180:
 print("obtuse angle triangle")
elif A+B+C==90:
 print("right angle triangle")
elif A+B+C==60:
  print("acute angle") 
else:
 print("NONE")