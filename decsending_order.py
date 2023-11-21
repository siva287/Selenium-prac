my_list = [26, 14, 24, 13, 5]
for i in range(0, len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] < my_list[j]:
            my_list[i], my_list[j] =  my_list[j],  my_list[i]
print(my_list)
my_list = [26, 15, 18, 16, 14, 24, 13, 5]
for i in range(0, len(my_list)):
    for j in range(i+1, len(my_list)):
        if my_list[i] < my_list[j]:
            tem = my_list[i]
            my_list[i] = my_list[j]
            my_list[j] = tem
print(my_list)
