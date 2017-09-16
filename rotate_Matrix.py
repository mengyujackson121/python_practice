def rotate_matrix(matrix):
    new_matrix = list(zip(*matrix))
    final = []
    for each in new_matrix:
        final.append(list(each[::-1]))
    return final


def test1():
    input_matrix = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
    output_matrix =[[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]
    assert(rotate_matrix(input_matrix) == output_matrix)


def test2():
    input_matrix = [[1, 2, 3, 4],
                    [4, 5, 6, 7],
                    [7, 8, 9, 0],
                    [1, 2, 3, 4]]
    output_matrix =[[1, 7, 4, 1],
                    [2, 8, 5, 2],
                    [3, 9, 6, 3],
                    [4, 0, 7, 4]]
    assert(rotate_matrix(input_matrix) == output_matrix)


def main():
    test1()
    test2()

if __name__ == '__main__':
    main()