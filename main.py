# ********************-:List Programs:-*******************

# 1.Python program to interchange first and last elements in a list


arr_list = [10, 20, 30, 40, 50]

arr_len = len(arr_list)
temp = arr_list[0]

arr_list[0] = arr_list[arr_len - 1]
arr_list[arr_len - 1] = temp

print(arr_list)


# ************2nd Ways to solve this using list core method*************

def first_to_last(a_list):
    first_index = a_list.pop(0)
    last_index = a_list.pop(-1)
    a_list.insert(0, last_index)
    a_list.append(first_index)
    return a_list


array_list = [10, 20, 30, 40, 50]

print(first_to_last(array_list))

# 2.Python program to swap two elements in a list


ele_list = [10, 20, 30, 40, 50]

first_position = 2
second_position = 4

temp = ele_list[first_position - 1]
ele_list[first_position - 1] = ele_list[second_position - 1]
ele_list[second_position - 1] = temp

print("list after", first_position, "nd and", second_position, "th", "elements interchange:", ele_list)

# 3.Check if element exists in list in Python


l_list = [10, 20, 30, 40, 50]

num = int(input("Enter the number :"))

for i in l_list:
    if i == num:
        print(num, "is Available")

# 4.Different ways to clear a list in Python

l_list = [10, 20, 30, 40, 50]
print(l_list)
del l_list[:]
print(l_list)

# another one using clear method

l_list = [10, 20, 30, 40, 50]
print(l_list)
l_list.clear()
print(l_list)

# 5.Reversing a List in Python

l_list = [11, 22, 33, 44, 55]
l_len = len(l_list)

n_list = l_list[::-1]

print("Reverse List: ", n_list)

# 6.Python program to find sum of elements in list

l_list = [10, 20, 30, 40, 50]
Total = 0

for i in l_list:
    Total = Total + i

print("Sum of elements :", Total)

# 7.Python | Multiply all numbers in the list

l_list = [4, 5, 6, 7]

Total = 1

for i in l_list:
    Total = Total * i

print("Product of elements :", Total)

# 8.Python program to find smallest number in a list

l_list = [30, 20, 70, 10, 80]
l_min = l_list[0]

for i in l_list:
    if i < l_min:
        l_min = i

print("Minimum list item:", l_min)

# 9.Python program to find largest number in a list

l_list = [30, 20, 70, 10, 80]
l_max = l_list[0]

for i in l_list:
    if i > l_max:
        l_max = i

print("Maximum list item:", l_max)

# 10.Python program to find second largest number in a list

l_list = [10, 15, 70, 18, 16]
l_len = len(l_list)
l_second = l_first = l_list[0]

for i in range(1, l_len):
    if l_list[i] > l_first:
        l_second = l_first
        l_first = l_list[i]

    elif l_second < l_list[i] < l_first:
        l_second = l_list[i]

print("Largest elements:", l_first)
print("Second Largest elements:", l_second)

# Python program to find N largest elements from a list
