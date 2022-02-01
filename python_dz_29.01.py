my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
new_list = []
for this_list in my_list:
    if  this_list > 100:
            new_list.append(this_list)

# new_list = new_list[::-1]
# while len(new_list) > 0:
#     print(new_list.pop())

for that_list in new_list:
    if that_list > 0:
        print(that_list)

####################################

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
my_results = []
for list in my_list:
    if  list > 100:
            my_results.append(list)
print(my_results)

####################################

my_list = [1, 2, 3, 4, 5]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
elif len(my_list) >= 2:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)

###################################

my_string ='0123456789'
my_string_1 ='0123456789'
my_list = []
my_list_1 = []
for symb_1 in my_string:
    for symb_2 in my_string_1:
        my_list.append(symb_1 + symb_2)
for int_1 in my_list:
    if int_1.isdigit():
        int_1 = int(int_1)
        my_list_1.append(int_1)
print(my_list_1)










