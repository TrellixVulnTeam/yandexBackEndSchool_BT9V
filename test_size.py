import sys
arr = ['a' * 100 for i in range(0, 10 ** 6)]
arrNum = [10 for i in range(0, 10 ** 6)]
simple_string = ''
simple_string = 'a' * 100 * 10 ** 6
print(sys.getsizeof(arr))
print(sys.getsizeof(simple_string))
print(sys.getsizeof(arrNum))
print(sys.getsizeof('a' * 100))