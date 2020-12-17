#Different types of tuple
#empty tupple
my_tuple=()
print(my_tuple)

#tuple having integers
my_tuple=(1,2,3)
print(my_tuple)

#my_tuple mixed datatypes
my_tuple=(1,"Hello",3)
print(my_tuple)

#nested tuple
my_tuple=("mouse",[8,4,6],(1,2,3))
print(my_tuple)


#index
my_tuple=('p','r','o','g','r','a','m')
print(my_tuple[0])
print(my_tuple[1])


n_tuple=("mouse",[8,4,6],(1,2,3))
print(n_tuple[0][3])
print(n_tuple[1][2])

#negative Indexing
my_tuple=('p','r','o','g','r','a','m')
print(my_tuple[-1])
print(my_tuple[-6])

#slicing
my_tuple=('p','r','o','g','r','a','m')
print(my_tuple[1:4])

#iteration through the tuple

length=len(my_tuple)

#for i in my_tuple:
  #  print(i)
for i in range(length):
    print(my_tuple[i])
