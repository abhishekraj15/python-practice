abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> userscore = input("Give me a score value: ")
Give me a score value: 200
>>> userscore
'200'
>>> userscore / 2
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    userscore / 2
    ~~~~~~~~~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> userscore_in_int = int(userscore)
>>> userscore_in_int
200
>>> 