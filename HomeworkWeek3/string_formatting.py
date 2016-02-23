# i is first in every row: 0, 5, 10...
for i in range(0, 1001, 5):
    # j is the numbers in the row: 0, 1, 2, 3, 4
    for j in range(5):
        # format string
        # before the colon is the position of the argument
        # 0 is the fill char
        # > indicates right align (< left ^ center)
        # 5d means 5 digits
        # " " separated by space
        # end="" forces inline print
        print('{:0>5d}'.format(i + j), " ", end="")
    # five in a row
    print()
