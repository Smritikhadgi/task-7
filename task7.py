# 1. Write a Python program to get the smallest number from a list.
# a=[5,10,98,75,65]
# print("Minimum is:", min(a))

# 2.  Write a Python function to check a list is empty or not.
# a=[]
# if len(a):
#     print("List is not empty")
# else:
#     print("List is empty")

# 3.  Write a Python program to select an item randomly from a list.
# import random
# a=["Python",29,"Ram"]
# print(random.choice(a))


# 4.  Write a Python program to copy a list.
# a=[8,52,67,98]
# b=[]
# b=a.copy()
# print(b)

# 5.  Write a Python program to find the 2nd largest number in a list.
# a=[66,98,75,45,12,39,30]
# print(sorted(a)[-2])

# 6.  Write a Python program to print a specified list after removing the 3rd elements.
# a=["Language","Python",65,28,31.5]
# del a[2]
# print(a)


# 7. Write a Python program to count the number of even and odd numbers from a series of numbers.
# a=[2,98,75,65,96,41]
# count_odd=0
# count_even=0
# for i in a:
#     if i%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# print("Numbers of even numbers:",count_even)
# print("Numbers of odd numbers:",count_odd)

# 8. Write a Python program to add an item in a tuple.
# a=(99,65,75,42)
# list=list(a)
# list.insert(1,25)
# b=tuple(list)
# print(b)

# 9.  Write a Python program to convert tuple to list.
# a=(66,89,75,95,96)
# list=list(a)
# print(list)

# 10.  Write a Python program to convert a tuple to a string.
# a=("Python","is","Language")
# b=''.join(a)
# print(b)

# 11.  Write a Python program to convert a list to a tuple.
# a=[56,58,59,74,72]
# b=tuple(a)
# print(b)

# 12.  Write a Python Program to Convert List of Tuple into Dictionary
# a=[("Aakash",10),("Guarav",12),("Aanand",15),("Suraj",20),("Akhil",30)]
# b=dict()
# for student,score in a:
#     b.setdefault(student,[]).append(score)
# print(b)

# 13.  Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
# a={0:10,1:20}
# a.update({2:30})
# print(a)

# 14. Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# 15.  Write a Python script to check if a given key already exists in a dictionary.
# a={"Name":"Aakash","Address":"Dilibazar"}
# if "Address" in a:
#     print("Present")
# else:
#     print("Absent")

# 16.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# a=dict()
# for i in range(1,16):
#     a[i]=i**2
# print(a)

# 17. Write a Python script to merge two Python dictionaries.
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic1.update(dic2)
# print(dic1)

# 18. Write a Python program to find the 3nd largest number in a list.
# a=[66,98,75,45,12,39,30]
# print(sorted(a)[-3])

# 19. Write a Python program to create a set.
# a=set([0,1,2,3,4,5])
# print(a)

# 20. Write a Python program to iteration over sets.
# a=set("Programming")
# for val in a:
#     print(val)

# 21. Write a Python program to add member(s) in a set.
# data={1,2,3,4}
# data2={5,6,7}
# data.update(data2)
# print(data)


#  22. Write a Python program to remove item(s) from set
# data={1,2,3,4,5,6}
# data1={2,6}
# data.difference_update(set(data1))
# print(data)

# 23. Write a Python program to remove an item from a set if it is present in the set.
# a={"lemon","cat","cherry"}
# a.discard("cat")
# print(a)

# 24. Write a Python program to create an intersection of sets. 
# a={2,3,4,5,6,7}
# b={5,6,7,8,9,10}
# c= a & b
# print(c)

# 25. Write a Python script to check if a given key exists in a dictionary.
# a={"Name":"Aakash","Address":"Dilibazar"}
# if "Address" in a:
#     print("Present")
# else:
#     print("Absent")

# 26. Write a Python script to check if a given values exists in a dictionary.
a={"Name":"Aakash","Address":"Dilibazar"}
if "Aakash" in a.values():
    print("Present")
else:
    print("Absent")