def min_coins_required_to_make_a_change(denominations, value):
    """
    Given a value, we need to determine the minimum number of
    coins from the given denomination set that are required
    to make change for the above mentioned value. There is an
    infinite supply of each denomination.
    :param denominations: List containing the available denominations
    :param value: Value for which a change is required
    :return: Minimum number of coins required to make the change
    """
    import decimal

    if value == 0:
        return 0

    if value < 0:
        return -1

    result = decimal.Decimal('Infinity')

    for i in xrange(len(denominations)):
        if denominations[i] <= value:
            sub_result = min_coins_required_to_make_a_change(denominations, value-denominations[i])

            if sub_result != decimal.Decimal('Infinity') and sub_result + 1 < result:
                result = sub_result + 1

    return result


def dynamic_programming_solution(denominations, value):
    """
    The dynamic programming solution of the algorithm is
    given by this function.
    :param denominations: List containing the available denominations
    :param value: Value for which a change is required
    :return: Minimum number of coins required to make the change
    """
    import decimal

    dp_array = [decimal.Decimal('Infinity')] * (value+1)

    dp_array[0] = 0  # for the base case

    for i in xrange(len(dp_array)):
        for j in xrange(i):
            sub_result = dp_array[i-denominations[j]]
            if sub_result != decimal.Decimal('Infinity') and sub_result + 1 < dp_array[i]:
                dp_array[i] = sub_result + 1

    return dp_array[value]
