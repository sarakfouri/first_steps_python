import numpy as np
my_array1 = np.array([1,2,3,4,5,6,7,8,9,10])
print(my_array1)

print(my_array1[2:6])
print(my_array1[3])
print(my_array1[7:])
print(my_array1[::2])

#1.5 use slicing with step-parameter to print out the elements holding numbers 1,3,5 in my_array1.
print(my_array1[:5:2])
#1.6 use slicing with step-parameter to print out the elements holding numbers 6,8,10 in my_array1.
print(my_array1[5:10:2])
#1.7 use slicing with step-parameter to print out the elements holding numbers 2,5,8 in my_array1.
print(my_array1[1:9:3])
#1.8 use negative slicing to print out the elements holding numbers 8,9,10 in my_array1.
print(my_array1[7::])
#1.9 use negative slicing with step-parameter to print out the elements holding numbers 6,8,10 in my_array1.
print(my_array1[5:10:2])
#1.10 use slicing to print out the elements holding numbers 3,5,7 in my_array1.
print(my_array1[2:7:2])


#TASK 2

my_array2 = np.array( [[1,2,3,4],[5,6,7,8],[9,10,11,12]] )
print(my_array2)

#2.1 use slicing to print out the elements holding numbers 6,7,8 in my_array2.

print(my_array2[1,1])
#32.2 use slicing with step to print out the elements holding numbers 9,11 in my_array2

print(my_array2[2, 0:3:2])
#2.3 use slicing with step to print out the elements holding numbers 1,3,5,7,9,11 in my_array2
print(my_array2[:,::2])
#2.4 use slicing with step to print out the elements holding numbers 1,4,5,8,9,12 in my_array2

print(my_array2[:,::3])
#2.5 use negative slicing to print out the elements holding numbers 3,4,7,8,11,12 in my_array2

print(my_array2[:,:-3:-1])
#2.6 use negative slicing to print out the elements holding numbers 2,3,6,7,10,11 in my_array2
print(my_array2[:,-3::-1])
#2.7 use negative slicing with step to print out the elements holding numbers 2,4,6,8,10,12 in my_array2
print(my_array2[:,-3::2])
#2.8 use negative slicing with step to print out the elements holding numbers 1,3,5,7,9,11 in my_array2
print(my_array2[:,-4::2])


sheet1 = np.array( [[1,2,3,4],[5,6,7,8],[9,10,11,12]] )
sheet2 = np.array( [[13,14,15,16],[17,18,19,20],[21,22,23,24]] )
sheet3 = np.array( [[25,26,27,28],[29,30,31,32],[33,34,35,36]] )

my_array3=np.array([sheet1,sheet2,sheet3])
print(my_array3)

#3.1 use slicing to print out the elements holding numbers 33,34,35 in my_array3.

print(my_array3[2,2, :3])
#3.2 use slicing with step to print out the elements holding numbers 30,32 in my_array3
print(my_array3[2,1, 1:4:2])
#3.3 use slicing with step to print out the elements holding numbers 25,27,29,31,33,35 in my_array3
print(my_array3[2,:,:10:2 ])
#3.4 use slicing with step to print out the elements holding numbers 13,16,17,20,21,24 in my_array3
print(my_array3[1,:,::3])
#3.5 use negative slicing to print out the elements holding numbers 15,16,19,20,23,24,27,28,31,32,35,36 in my_array3
print("here")
print(my_array3[1:, : ,:-3:-1])
#3.6 use negative slicing with step to print out the elements holding numbers 14,16,18,20,22,24,26,28,30,32,34,36 in my_array3
print("here")
print(my_array3[1:, :, -3::2])