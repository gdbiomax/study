import random
from random import randint

array           =   [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]



def get_avaliable_list(row_index,col_index):
    list = [1,2,3,4,5,6,7,8,9]
    for item in get_row_data_list(row_index):
        if item in list:
            list.remove(item)
    for item in get_col_data_list(col_index):
        if item in list:
            list.remove(item)
    for item in get_3x3_list(row_index,col_index):
        if item in list:
            list.remove(item)
    return list


def get_row_data_list(row_index):
    list = []
    for i in range(9):
        list.append(array[row_index][i])
    return list


def get_col_data_list(col_index):
    list = []
    for i in range (9):
        list.append(array[i][col_index])
    return list

def get_3x3_list(row_index,col_index):
    list = []
    start_row = int(row_index / 3) * 3
    start_col = int(col_index / 3) * 3
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            list.append(array[i][j])
    return list


def fill_in():
    maxTemp = 100
    count = 9999
    while count > maxTemp:
        for i in range(9):
            for j in range(9):
                array [i][j] = 0

        for row in range(9):
            for col in range(9):
                count = 0
                randVal = 0
                while randVal in get_row_data_list(row) or randVal in get_col_data_list(col) or randVal in get_3x3_list(row,
                                                                                                                        col):
                    count += 1
                    randVal = random.randint(1, 9)
                    if count > maxTemp: break
                array[row][col] = randVal
                if count > maxTemp: break
            if count > maxTemp: break
                #
                # if not get_avaliable_list(row,col):
                #     pass
                #     # return False
                #     #break
                # else:
                #     count += 1
                #     array[row][col] = random.choice(get_avaliable_list(row,col))
                # if count > maxTemp: break


fill_in()

for item in array:
    print item












