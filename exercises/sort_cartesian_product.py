import itertools
def sort_cartesian_product(list_one, list_two):
    """ Return sorted Cartesian product.

    >>> Cartesian product([1, 5, 6], [0, 3, 7])
    [[0, 1], [1, 3], [1, 7], [0, 5], [3, 5], [5, 7], [0, 6], [3, 6], [6, 7]]
    """
    # NOTE: You can initialize fixed size earlier int type in this case.
    #       Array v/s linked-lists (sort of).
    res = [0]*len(list_one)*len(list_two)

    count = 0
    for i in list_one:
        for j in list_two:
            res[count] = sorted([i, j])
            count += 1


    return(res)



# Do not make any changes to the code below
# Function used in main() to print
# what each function returns vs. what it's supposed to return

def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{0} returned: {1} expected: {2}'.format(prefix, repr(returned), repr(expected)))


# Do not make any changes to the code below
# Calls the above functions with interesting inputs.
def main():
    print('sort_cartesian_product')
    test(sort_cartesian_product([1, 5, 6], [0, 3, 7]),
                                [[0, 1], [1, 3], [1, 7], [0, 5], [3, 5],
                                [5, 7], [0, 6], [3, 6], [6, 7]])


if __name__ == '__main__':
    main()
