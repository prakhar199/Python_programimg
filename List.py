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


#Demonstration of list insert() method
odd1=[1,9]
odd1.insert(1,3)
print("The list after insert() function is: ",odd1)


#Deleting the list items
my_list1=['p','r','o','g','r','a','m','i','s','g','o','o','d']
del my_list1[2]
print(my_list1)

#Deleting the multiple elements from the list
my_list1=['p','r','o','g','r','a','m','i','s','g','o','o','d']
del my_list1[1:5]
print(my_list1)

#remove() to remove a element
my_list1=['p','r','o','g','r','a','m','i','s','g','o','o','d']
my_list1.remove('p')
print(my_list1)

#pop()
my_list1=['p','r','o','g','r','a','m','i','s','g','o','o','d']
print(my_list1.pop(2))

#clear()
my_list1.clear()
print(my_list1)

#sort()
vowels=['e','a','u','o','i']
vowels.sort(reverse=True)
print("Sorted list is :",vowels)

numbers=[1,5,7,4,3,7,8,9]
numbers.sort(reverse=True)  #descending
numbers.sort() #ascending
print("Sorted number list is: ",numbers)

numbers1=[5,6,9,8,3]
numbers1.sort()
numbers1.reverse()
print("Sorted and reversed list is: ",numbers1)

#index()
vowels=['e','a','u','o','i']
location=vowels.index('a')
print("The index of the element in the list is: ",location)

#count()
vowels=['e','a','u','o','i','i']
print(vowels.count('i'))

