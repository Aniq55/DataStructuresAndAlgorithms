def get_length_of_longest_increasing_subsequence(array):
    """
    The function uses dynamic programming to calculate the length of
    longest increasing subsequence in a given array

    :param array: Input array whose longest increasing subsequence is
                  to be calculated
    :return: Length of the longest increasing subsequence
    """
    lis_array = [1] * len(array)
    for i in xrange(1, len(array)):
        for j in xrange(i):
            if array[j] < array[i] and lis_array[j] + 1 > lis_array[i]:
                lis_array[i] = lis_array[j]+1
    return max(lis_array)


if __name__ == '__main__':
    input_array = map(int, raw_input("Enter the elements: ").split())
    lis_length = get_length_of_longest_increasing_subsequence(input_array)
    print "Length of longest increasing subsequence is:", lis_length
