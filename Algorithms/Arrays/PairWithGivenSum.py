def pair_with_given_sum_exists_hash_method(array, xsum):
    """
    The function returns True or false based on whether
    a pair with sum 'xsum' exists in the array.
    :param array: Array of numbers
    :param xsum: Given sum
    :return: Boolean value True or False
    """
    mydict = {}
    count = 0

    for element in array:
        if (xsum-element) in mydict:
            count += 1
            print "The pair is (%s, %s)" % (element, xsum-element)
        mydict[element] = 1

    if count == 0:
        return False
    else:
        return True


def main():
    array = [1, 4, 45, 6, 10, -8]
    xsum = 16
    pair_with_given_sum_exists_hash_method(array,xsum)

if __name__ == '__main__':
    main()
