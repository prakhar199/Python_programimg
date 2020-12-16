my_list=['p','r','o','b','e']

print(my_list[0])

print(my_list[2])

print(my_list[4])

#nested list
n_list=["happy", [2,0,1,5]]

print(n_list)

print(n_list[0])

print(n_list[1])
 #printing list within a list
print(n_list[1][2])

#finding the length of list within a list
len_list=len(n_list[1])
#accessing the elements of list within a list 
for i in range(len_list):
    print(n_list[1][i])

#negative indexing
print(my_list[-1])
print(my_list[-5])

#slicing

my_list1=['p','r','o','g','r','a','m','i','s','g','o','o','d']

print(my_list1[2:5])

#element begining from 4th from the last 
print(my_list1[ : -5])

#Correction mistaken values in the list
odd=[2,4,6,8]

#change the 1st element
odd[0]=1

print(odd)

#change the values from 2nd to 4th item

odd[1:4]=[3,4,7]

print(odd)

#append()

odd.append(9)

print(odd)

#extend()

odd.extend([11,13,15])
print(odd)

print(odd+[17,19,21]) #concatination of lists


