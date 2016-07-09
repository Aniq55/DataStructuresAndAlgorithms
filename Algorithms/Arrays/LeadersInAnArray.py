def get_leaders(a):
    """
    Returns a list of leaders in an array. A leader is an element in an array
    which does not have any number greater than it on it's right.
    :param a: Input array
    :return: Array of leaders
    """
    max = a[-1]
    leaders = []
    leaders.append(a[-1])

    for e in reversed(a):
        if e > max:
            max = e
            leaders.append(e)

    return leaders

if __name__ == '__main__':
    a = [16, 17, 4, 3, 5, 2]
    x = get_leaders(a)

    print x