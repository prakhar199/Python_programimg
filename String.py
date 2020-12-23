my_string='Hello'
print(my_string)

my_string="Hello"
print(my_string)

line="""Hello, welcome
the world of python.
Prakhar"""

print(line)

str="python"
print("str ",str)

#first character
print('str[0] : ', str[0])

#last character
print('str[-1] : ', str[-1])

#slicing 2nd to 5th character
print(str[1:5])

#slicing 6th to 2nd last character

print(str[-5:-1])

#String are immutable.
#my_string[0]='T'
#print(my_string)
#TypeError: 'str' object does not support item assignment

del my_string

#concatenation operation
str1="Hello"
str2="World!"
print("str1+str= ", str1+str2)
print("str1*3= ", str1*3)


#Iterating through a string
count=0
length=len("Hello World")
print(length)
for letter in 'Hello World':
    if(letter=='l'):
        count+=1
print(count, "times letters found")





