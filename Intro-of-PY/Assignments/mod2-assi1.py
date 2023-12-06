# Write a program to make another list of duplicate elements from the following list
# [1, 5, 6, 5, 1, 2, 3]

my_list = [1, 5, 6, 5, 1, 2, 3]
new_list = []

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] == my_list[j] and my_list[i] not in new_list:
            new_list.append(my_list[i])

print(new_list)


