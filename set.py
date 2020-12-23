#Different types of sets in python
my_set={1,2,3}
print(my_set)

#set of mixed datatype

my_set={1.0, "Hello", (1,2,3)}
print(my_set)

#single element insertion
my_set={1,3}
my_set.add(2)
print(my_set)

#multiple element insertion
my_set.update([7,6,5])
print(my_set)

#add of list and set
my_set.update([10,11],{1,12,18}, "HelloWorld")
print(my_set)

my_set={"Hello World", "Prakhar"}
print(my_set)
print(my_set.pop())
print(my_set.pop())

A={1,2,3,4,5}
B={4,5,6,7,8}
print(A.union(B))  #A|B

print(A.intersection(B))   #aA&B

print(A.difference(B))   #A-B

print(A.symmetric_difference(B))   #A^B

my_set={"apple", "mango", "pineapple"}
j=0
for i in my_set:
    j=+1
    if(i=="apple"):
        print("Apple found location : ", j)
        






