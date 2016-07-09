def get_excel_cell_address_from_numeric_value(value):
    """
    Given the cell number of an excel cell, return the alphanumeric representation.
    :param value: cell number
    :return: alphanumeric representation of cell address
    """
    my_dict = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
               10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q',
               18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y',
               26: 'Z'}

    answer = ''

    while value:
        q = value % 26
        answer = my_dict[q] + answer
        value /= 26

    return answer


def get_excel_cell_address_from_alphnumeric_value(a_value):
    """
    Given the alphanumeric representation of the cell number of an excel cell, return the numeric value.
    :param a_value: alphanumeric representation of cell address
    :return: cell number
    """
    my_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
               'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
               'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
               'Z': 26}
    i = 0
    num = 0

    for e in reversed(a_value):
        num += my_dict[e] * (26**i)
        i += 1

    return num

if __name__ == '__main__':
    print get_excel_cell_address_from_numeric_value(1406)
    print get_excel_cell_address_from_alphnumeric_value('BBB')
