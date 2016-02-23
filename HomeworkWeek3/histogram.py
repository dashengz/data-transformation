def histogram(an_array):
    """
    Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
    For example, histogram([4, 9, 7]) should print the following:
        ****
        *********
        *******

    :param an_array: a list of numbers (positive integers?)
    :return: a histogram of the list
    """
    # special cases
    if not an_array:
        print("Oops! Empty array!")
    for num in an_array:
        if num == 0:
            print("Zero(0) detected! ")
        elif num < 0:
            print("Negative number detected! ")
        elif int(num) != num:
            print("Float detected! ")
        else:
            print("*" * num)


def modified_histogram(an_array):
    # special cases
    if an_array is None:
        print("Oops! Empty array! ")
    # sort array
    an_array.sort()
    # iterate through the list and print histogram
    for num in an_array:
        if num < 0:
            print("Negative number detected! (%s)" % num)
        elif int(num) != num:
            print("Float detected! (%s)" % num)
        else:
            print("*" * num + "(%s)" % num)


# tests
histogram([4, 9, 7])
histogram([9, 4, 7])
histogram([])
histogram([0])
# hmmm what should these do?
histogram([-1])
histogram([1, 2, 3.14159])
# histogram(range(6, 300, 12))

# tests
modified_histogram([4, 9, 7])
modified_histogram([9, 4, 7])
modified_histogram([])
modified_histogram([0])
# hmmm what should these do?
modified_histogram([-1])
modified_histogram([1, 2, 3.14159])
