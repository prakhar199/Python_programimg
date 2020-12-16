a=float(input("Enter the length of the 1st side"))
b=float(input("Enter the length of the 2nd side"))
c=float(input("Enter the length of the 3rd side"))

s=(a+b+c)/2

area= (s*(s-a)*(s-b)*(s-c))

print("the area of the triangle is", area)
