abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> x = 2
>>> y = 3
>>> z = 4
>>> x+y
5
>>> x**x
4
>>> y**y
27
>>> (x + y) * z
20
>>> x+(y*z)
14
>>> 40 + 2.23
42.23
>>> 'hiteshi" + 3
  File "<python-input-9>", line 1
    'hiteshi" + 3
    ^
SyntaxError: unterminated string literal (detected at line 1)
>>> 'hiteshi' + 3
Traceback (most recent call last):
  File "<python-input-10>", line 1, in <module>
    'hiteshi' + 3
    ~~~~~~~~~~^~~
TypeError: can only concatenate str (not "int") to str
>>> int(2.23)
2
>>> 40 + int(2.23)
42
>>> float(40) + 2.23
42.23
>>> float(40)
40.0
>>> 'chai' + 'code'
'chaicode'
>>> x , y, z
(2, 3, 4)
>>> x + 1, y * 2
(3, 6)
>>> y % 2
1
>>> z ** 2
16
>>> 100 ** 2
10000
>>> 2 ** 100
1267650600228229401496703205376
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>> result = 1/3.0
>>> result
0.3333333333333333
>>> repr('chai')
"'chai'"
>>> str('chai')
'chai'
>>> print('chai')
chai


>>> 1 < 2
True
>>> 2>1
True
>>> 2<1
False
>>> 5.0 == 5.0
True
>>> 5.0 == 5
True
>>> 4.0 != 5.0
True
>>> x, y ,z
(2, 3, 4)
>>> x < y < z
True
>>> x < y and y < z
True
>>> x < z or y < z
True
>>> 1 == 2 < 3
False
>>> 1 == 2 and 2 < 3
False
>>> import math
>>> math.floor(3.5)
3
>>> math.random()
Traceback (most recent call last):
  File "<python-input-42>", line 1, in <module>
    math.random()
    ^^^^^^^^^^^
AttributeError: module 'math' has no attribute 'random'
>>> math.floor(-3.5)
-4
>>> math.floor(3.6)
3
>>> math.trunc(2.8)
2
>>> math.trunc(-2.8)
-2
>>> 9999999999999999999999999999999999999999999 + 1
10000000000000000000000000000000000000000000
>>> 9999999999999999999999999999999 * 2.1
2.1e+31
>>> 2 * 200
400
>>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376


>>> 2 + 1j
(2+1j)
>>> 2 + 1j * 3
(2+3j)
>>> (2 + 1j) * 3
(6+3j)


>>> 0o20
16
>>> 0xFF
255
>>> 0b1000
8
>>> oct(64)
'0o100'
>>> hex(64)
'0x40'
>>> bin(64)
'0b1000000'
>>> int(3.14)
3
>>> in(64)
  File "<python-input-61>", line 1
    in(64)
    ^^
SyntaxError: invalid syntax
>>> int(64)
64
>>> int("64", 8)
52
>>> int("64", 16)
100
>>> int("10000", 2)
16
>>> x = 1
>>> x << 2
4
>>> x | 2
3
>>> 