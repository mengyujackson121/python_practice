def zero_matrix(m):
    row_m = 0
    row_list = []
    column_list = []
    # find out what needs to be zero
    for row in m:
        element_m = 0
        for element in row:
            if element == 0:
                row_list.append(row_m)
                column_list.append(element_m)
            element_m += 1
        row_m += 1

    # Set rows to zero
    for row_num in row_list:
        m[row_num] = [0]*len(m[row_num])
    m = list(zip(*m))
    for col_letter in column_list:
        m[col_letter] = [0]*len(m[col_letter])
    m = list(zip(*m))
    m = (list(list(row) for row in m))
    return m


def zero_matrix2(m):
    #row_m = 0
    row_list = set()
    column_list = set()
    # find out what needs to be zero
    for row_m, row in enumerate(m):
        #element_m = 0
        for element_m, element in enumerate(row):
            if element == 0:
                row_list.add(row_m)
                column_list.add(element_m)
        #    element_m += 1
        #row_m += 1

    # Set rows to zero
    for row_num in row_list:
        m[row_num] = [0]*len(m[row_num])

    for col_letter in column_list:
        for row in m:
            row[col_letter] = 0
    return m


def zero_matrix3(m):
    row_m = 0
    row_list = list()
    column_list = list()
    # find out what needs to be zero
    for row in m:
        element_m = 0
        for element in row:
            if element == 0:
                row_list.append(row_m)
                column_list.append(element_m)
            element_m += 1
        row_m += 1

    # Set rows to zero
    for row_num in row_list:
        m[row_num] = [0]*len(m[row_num])

    for col_letter in column_list:
        for row in m:
            row[col_letter] = 0
    return m
def test1():
    input_matrix = [[1, 2, 3],
                    [4, 0, 6],
                    [7, 8, 9]]


    output_matrix =[[1, 0, 3],
                    [0, 0, 0],
                    [7, 0, 9]]
    assert(zero_matrix(input_matrix) == output_matrix)


def test2():
    input_matrix = [[0, 2, 3, 4],
                    [4, 5, 6, 7],
                    [7, 8, 9, 0],
                    [1, 2, 3, 4]]


    output_matrix =[[0, 0, 0, 0],
                    [0, 5, 6, 0],
                    [0, 0, 0, 0],
                    [0, 2, 3, 0]]
    assert(zero_matrix(input_matrix) == output_matrix)

def test_big():
    import random
    import time
    import copy
    import math
    for i in range(0, 5001, 500):
        input_matrix = []
        for r in range(i):
            new_row = []
            for c in range(i):
                new_row.append(random.randint(0, int(math.sqrt(i)) + 1))
            input_matrix.append(new_row)
        c1 = copy.deepcopy(input_matrix)
        c2 = copy.deepcopy(input_matrix)
        start_time = time.time()
        zero_matrix2(c1)
        mid_time = time.time()
        zero_matrix3(c2)
        end_time = time.time()
        print(i, mid_time - start_time, end_time - mid_time)


def main():
    test1()
    test2()
    test_big()

if __name__ == '__main__':
    main()