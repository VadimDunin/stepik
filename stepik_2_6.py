def execise_3():
    # input_numbers = input()
    input_numbers = "3 2 4 5 3 67 7 5 435 4 347 78 6 5 67 -3 -4 -2"
    # search_number = input()
    search_number = "6666"
    array_with_no_spaces = []
    output_array = []
    # for number in input_numbers:
    #     if number != " ":
    #         array_with_no_spaces.append(number)
    array_with_no_spaces = input_numbers.split(" ")
    print("array_with_no_spaces " + str(array_with_no_spaces))
    i = 0
    for element in array_with_no_spaces:
        if int(search_number) == int(element):
            output_array.append(str(i))
            output_array.append(" ")
        i += 1
    if len(output_array) != 0:
        out_str = ''.join(output_array)
        print(out_str)
    else:
        print('Отсутствует')


def execise_4():
    preambule = """
        Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк, заканчивающихся строкой, содержащей только строку "end" (без кавычек)
        Программа должна вывести матрицу того же размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы.
        В случае одной строки/столбца элемент сам себе является соседом по соответствующему направлению.
        """


    output_matrix = []

    matrix = read_matrix_input()

    #print(int(matrix[2][0])+int(matrix[0][0]))
    output_matrix = matrix
    i = 0
    j = 0

    # print(matrix[0][0])
    # print(matrix[0][1])
    # print(matrix[0][2])

    # print(len(matrix[0]))

    print_2D_matrix(upgrade_matrix(matrix))

    # while(j<len(matrix)):
    #     while (i < len(matrix[j])):
    #         print(matrix[j][i])
    #         # output_matrix[i, j] = int(matrix[i-1, j])+int(matrix[i+1, j])+int(matrix[i, j-1])+int(matrix[i, j+1])
    #         i += 1
    #     if i>=len(matrix[j]):
    #         i = 0
    #     j += 1
    #print(matrix)


def upgrade_matrix(matrix):
    output_matrix = matrix
    i = 0
    j = 0
    while (int(i) < len(matrix)):
        while (int(j) < len(matrix[i])):
            try:
                output_matrix[i][j] = matrix[i-1][j] + matrix[i+1][j] + matrix[i][j-1] + matrix[i][j+1]
            except IndexError:
                print(output_matrix[i][j]+" ошибка индекса")
            j += 1
        j = 0
        i += 1
    return output_matrix


def read_matrix_input(stop_input_symbol="end"):
    # Читает матрицу построчно, пока не будет введено слово stop_input_symbol
    matrix = []
    while (True):
        input_str = input()
        if input_str == str(stop_input_symbol):
            break
        else:
            matrix.append(input_str.split(" "))
    return matrix


def print_2D_matrix(matrix):
    # Должно выводить двухмерную матрицу в привычном виде
    i = 0
    while (int(i) < len(matrix)):
        out_str = ''.join(str(x + " ") for x in matrix[i])
        print(out_str)
        i += 1



execise_4()