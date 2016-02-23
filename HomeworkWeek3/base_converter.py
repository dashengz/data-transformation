from datetime import date

import histogram


def base_converter(decimal_integer):
    result = "int: {0:,}; hex: {1}; oct: {2}; bin: {3}". \
        format(decimal_integer, add_space(hex(decimal_integer), 4),
               add_space(oct(decimal_integer), 4), add_space(bin(decimal_integer), 4))
    return result


# def base_converter(decimal_integer):
#     result = "int: {0:,}; hex: {1}; oct: {2}; bin: {3}".format(decimal_integer, hex(decimal_integer), oct(decimal_integer), bin(decimal_integer))
#     return result


def add_space(number, stride):
    result = ' '.join([number[::-1][i:i + stride] for i in range(0, len(number[::-1]), stride)])
    return result[::-1]


# testing

print(base_converter(0))
print(base_converter(1))
print(base_converter(15))
print(base_converter(16))
print(base_converter(date.today().toordinal()))

for i in range(64):
    histogram.modified_histogram([i])
    print(base_converter(i))
