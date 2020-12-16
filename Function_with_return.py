def absolute_value(num):
    "This function returns the absolute vaue of the entered number"
    if num>5:
        return 10
    else:
        return 0

n=int(input("Enter the number: "))
r=absolute_value(n)
print("The absolute value is: ",r)
