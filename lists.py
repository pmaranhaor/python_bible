Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> our_list= [27, 46, -5, 17, 99]
>>> print(our_list)
[27, 46, -5, 17, 99]
>>> type(our_list)
<class 'list'>
>>> our_list = [1, 2, [3, 4, 5], 6, 7,8]
>>> our_list[2]
[3, 4, 5]
>>> our_list[2][0]
3
>>> our_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> our_table[0][1]
2
>>> our_table[1][2]
6
>>> our_table = [2][0]
>>> our_table = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> out_table[2][0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    out_table[2][0]
NameError: name 'out_table' is not defined
>>> our_table[2][0]
7
>>> 