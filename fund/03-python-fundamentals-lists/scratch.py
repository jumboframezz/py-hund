def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)


def read_string_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = striped_line.split(" ")
    return list(line)




list_numbers = [-2, -1, -3]

number = list_numbers.pop(list_numbers,-1)
print(number)