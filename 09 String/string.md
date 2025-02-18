>>> chai = "Masala Chai"
>>> first_char = chai[0]
>>> print(first__char)
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    print(first__char)
          ^^^^^^^^^^^
NameError: name 'first__char' is not defined. Did you mean: 'first_char'?
>>> print(first_char)
M
>>> chai
'Masala Chai'
>>> slice_chai = chai[0:6]
>>> print)slice_chai)
  File "<python-input-9>", line 1
    print)slice_chai)
         ^
SyntaxError: unmatched ')'
>>> print(slice_chai)
Masala
>>> chai[-1]
'i'
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list = [3:1]
  File "<python-input-14>", line 1
    num_list = [3:1]
                 ^
SyntaxError: invalid syntax
>>> num_list[3:1]
''
>>> 




abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[3:]
'3456789'
>>> num_list[:7]
'0123456'
>>> num_list[0:7:2]
'0246'
>>> num_list[0:7:3]
'036'
>>> 




>>> chai = "Masala Chai"
>>> chai
'Masala Chai'
>>> print(chai.lower())
masala chai
>>> print(chai.upper())
MASALA CHAI
>>> chai
'Masala Chai'
>>> 




abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> chai = "    Masala Chai   "
>>> chai
'    Masala Chai   '
>>> print(chai.strip())
Masala Chai
>>> chai = "Lemon Chai"
>>> print(chai.replace("Lemon", "Ginger"))
Ginger Chai
>>> chai
'Lemon Chai'
>>> 



abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> chai = "Lemon, Ginger, Masala, Mint"
>>> print(chai.split(", "))
['Lemon', 'Ginger', 'Masala', 'Mint']
>>> chai = "Masala Chai"
>>> chai
'Masala Chai'
>>> print(chai.find("Chai"))
7
>>> print(chai.find("chai"))
-1
>>> chai = "Mansala Chai Chai Chai"
>>> print(chai.count("Chai"))
3
>>> 



String to List
abhishekrajput@Abhisheks-MacBook-Air Python % python3
>>> chai_type = "Masala"
>>> quantity = 2
>>> order = "I ordered {} cups of chai"
>>> order
'I ordered {} cups of chai'
>>> print(order.format(quanity, chai_type))
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    print(order.format(quanity, chai_type))
                       ^^^^^^^
NameError: name 'quanity' is not defined. Did you mean: 'quantity'?
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of chai
>>> order = "I ordered {} cups of {} chai"
>>> print(order.format(quantity, chai_type))
I ordered 2 cups of Masala chai
>>> 


List to String
abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> chai_variety = ["Lemon", "Masala", "Ginger"]
>>> chai_variety
['Lemon', 'Masala', 'Ginger']
>>> print("".join(chai_variety))
LemonMasalaGinger
>>> print(" ".join(chai_variety))
Lemon Masala Ginger
>>> print("-".join(chai_variety))
Lemon-Masala-Ginger
>>> print(", ".join(chai_variety))
Lemon, Masala, Ginger
>>> 




>>> chai = "Masala Chai"
>>> print(len(chai))
11
>>> chai
'Masala Chai'
>>> for letter in chai:
...     print(letter)
...     
M
a
s
a
l
a
 
C
h
a
i
>>> 





abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> chai = "He said, "Masala chai is awesome" "
  File "<python-input-0>", line 1
    chai = "He said, "Masala chai is awesome" "
                      ^^^^^^
SyntaxError: invalid syntax
>>> chai = "He said, \"Masala chai is awesome\" "
>>> chai
'He said, "Masala chai is awesome" '
>>> chai = "Masala\nChai"
>>> chai
'Masala\nChai'
>>> print(chai)
Masala
Chai
>>> chai = r"Masala\nchai"
>>> chai
'Masala\\nchai'
>>> print(chai)
Masala\nchai
>>> chai = r"c:\user\pwd\"
  File "<python-input-9>", line 1
    chai = r"c:\user\pwd\"
           ^
SyntaxError: unterminated string literal (detected at line 1); perhaps you escaped the end quote?
>>> chai = r"c:\\user\\pwd\\"
>>> chai
'c:\\\\user\\\\pwd\\\\'
>>> print(chai)
c:\\user\\pwd\\
>>> chai = r"c:\user\pwd"
>>> print(chai)
c:\user\pwd
>>> 
























































