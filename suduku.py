import random
from random import randint

def get_avaliable_list(list):
    for number in row_data:
        if number in list:
            list.remove(number)
    for col in col_data:
        if col in list:
            list.remove(col)
    return list


row_data = []
col_data = []
for i in range(9):
    col_data.append([])

for i in range (9):
    index = 0
    
    while list:
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        list = get_avaliable_list(list)
        print list
        pick = random.choice(list)
        list.remove(pick)
        row_data.append(pick)
        col_data[index].append(pick)
        index += 1

print row_data
print col_data




