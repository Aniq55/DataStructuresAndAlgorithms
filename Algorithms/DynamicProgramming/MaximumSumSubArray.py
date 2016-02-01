def max_sum_subarray(array):
    """
    This function returns the maximum sum of a subarray that
    exists in the given array.
    :param array: Input array
    :return: Sum of the elements of the maximum sum subarray
    """
    all_negative = 1
    max_sum = 0
    current_sum = 0

    for e in array:
        if e >= 0:
            all_negative = 0
            break

    if all_negative == 1:
        return max(array)

    for i in xrange(len(array)):
        if current_sum + array[i] <= 0:
            current_sum = 0
        else:
            if current_sum + array[i] >= max_sum:
                max_sum = current_sum + array[i]
            current_sum += array[i]

    return max_sum


def max_sum_subarray_elegant(array):
    """
    Elegant python solution for the maximum sum subarray problem
    :param array: Input array
    :return: Sum of the maximum sum subarray
    """
    max_sum = array[0]
    current_sum = array[0]

    for i in xrange(1, len(array)):
        current_sum = max(array[i], current_sum+array[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def max_sum_subarray_brute_force():
    """
    Brute force solution for the maximum sum subarray problem
    :return: Sum of the elements of the maximum sum subarray
    """
    pass


def main():
    array = [-2, -3, 4, -1, -2, 1, 5, -3]
    array1 = [-2, -3, 3, -4, -1, 0, 1]
    max_sum = max_sum_subarray(array1)
    print max_sum

if __name__ == '__main__':
    main()