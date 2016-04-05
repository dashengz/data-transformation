# HomeworkWeek3
Familiarize with Python 3+.
Basic operations such as: print(), format(), join(),
for loop, lists, etc.
### Features:
- base_converter: Print out the bin/oct/hex of a decimal based number:
```
# Code
print(base_converter(0))
print(base_converter(1))
print(base_converter(15))
print(base_converter(16))
print(base_converter(date.today().toordinal()))

# Results
int: 0; hex: 0x0; oct: 0o0; bin: 0b0
int: 1; hex: 0x1; oct: 0o1; bin: 0b1
int: 15; hex: 0xf; oct: 0o17; bin: 0b 1111
int: 16; hex: 0x10; oct: 0o20; bin: 0b1 0000
int: 736,059; hex: 0xb 3b3b; oct: 0 o263 5473; bin: 0b 1011 0011 1011 0011 1011
```
- histogram: Takes a list of integers and prints a histogram to the screen:
```
# Code
histogram([4, 9, 7])

# Results
****(4)
*******(7)
*********(9)
```
- string_formatting: Format numbers from 0 to 1004:
```
# Results
00000  00001  00002  00003  00004
00005  00006  00007  00008  00009
00010  00011  00012  00013  00014
00015  00016  00017  00018  00019
00020  00021  00022  00023  00024
00025  00026  00027  00028  00029
00030  00031  00032  00033  00034
00035  00036  00037  00038  00039
...
```
- data_scraping: Scrap data from .txt file and filter.