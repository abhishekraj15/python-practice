>>> varities = ["Black", "Green", "Oolong", "White"]
>>> varities
['Black', 'Green', 'Oolong', 'White']
>>> print(varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[1])
Green
>>> print(varities[-1])
White
>>> print(varities[:])
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[:3])
['Black', 'Green', 'Oolong']
>>> print(varities[:1])
['Black']
>>> print(varities[:2])
['Black', 'Green']
>>> varities[3]
'White'
>>> varities[3] = "Herbal"
>>> print(varities)
['Black', 'Green', 'Oolong', 'Herbal']
>>> varities[1:2]
['Green']
>>> varities[1:2] = "Lemon"
>>> varities
['Black', 'L', 'e', 'm', 'o', 'n', 'Oolong', 'Herbal']
>>> varities = ["Black", "Green", "Oolong", "White"]
>>> varities
['Black', 'Green', 'Oolong', 'White']
>>> varities[1:2]
['Green']
>>> varities[1:2] = ["Lemon"]
>>> varities
['Black', 'Lemon', 'Oolong', 'White']
>>> varities[1:3]
['Lemon', 'Oolong']
>>> varities[1:3] = ["green", "Masala"]
>>> varities
['Black', 'green', 'Masala', 'White']
>>> 

>>> varities = ["Black", "Green", "Oolong", "White"]
>>> varities
['Black', 'Green', 'Oolong', 'White']
>>> print(varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[1])
Green
>>> print(varities[-1])
White
>>> print(varities[:])
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[:3])
['Black', 'Green', 'Oolong']
>>> print(varities[:1])
['Black']
>>> varities
['Black', 'green', 'Masala', 'White']
>>> varities[1:1]
[]
>>> varities[1:1] = ["test", "test"]
>>> varities
['Black', 'test', 'test', 'green', 'Masala', 'White']
>>> varities[1:2]
['test']
>>> varities[1:3]
['test', 'test']
>>> varities[1:3] = []
>>> varities
['Black', 'green', 'Masala', 'White']
>>> 



>>> varities = ["Black", "Green", "Oolong", "White"]
>>> varities
['Black', 'Green', 'Oolong', 'White']
>>> print(varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[1])
Green
>>> print(varities[-1])
White
>>> print(varities[:])
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[:3])
['Black', 'Green', 'Oolong']
>>> print(varities[:1])
['Black']
>>> varities
['Black', 'green', 'Masala', 'White']
>>> for item in varities:
...     print(item)
...     
Black
green
Masala
White
>>> for item in varities:
...     print(item, end="-")
...     
Black-green-Masala-White->>> 
>>> varities
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in varities:
...     print("I have Olong tea")
...     
>>> varities.append("Oolong")
>>> varities
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in varities:
...     print("I have Olong tea")
...     
I have Olong tea
>>> varities.pop()
'Oolong'
>>> varities
['Black', 'green', 'Masala', 'White']
>>> varities.remove("green")
>>> varities
['Black', 'Masala', 'White']
>>> varities.insert(1, "green")
>>> varities
['Black', 'green', 'Masala', 'White']
>>> varities
['Black', 'green', 'Masala', 'White']
>>> varities_copy = varities
>>> varities_copy
['Black', 'green', 'Masala', 'White']
>>> varities.insert(2, "Yellow")
>>> varities
['Black', 'green', 'Yellow', 'Masala', 'White']
>>> varities_copy
['Black', 'green', 'Yellow', 'Masala', 'White']
>>> varities_copy = varities.copy()
>>> varities_copy.insert(-1, "Orange")
>>> varities_copy
['Black', 'green', 'Yellow', 'Masala', 'Orange', 'White']
>>> varities
['Black', 'green', 'Yellow', 'Masala', 'White']
>>> 


>>> varities = ["Black", "Green", "Oolong", "White"]
>>> varities
['Black', 'Green', 'Oolong', 'White']
>>> print(varities)
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[1])
Green
>>> print(varities[-1])
White
>>> print(varities[:])
['Black', 'Green', 'Oolong', 'White']
>>> print(varities[:3])
['Black', 'Green', 'Oolong']
>>> print(varities[:1])
['Black']
>>> varities
['Black', 'green', 'Masala', 'White']
>>> for item in varities:
...     print(item)
...     
Black
green
Masala
White
>>> for item in varities:
...     print(item, end="-")
...     
Black-green-Masala-White->>> 
>>> varities
['Black', 'green', 'Masala', 'White']
>>> if "Oolong" in varities:
...     print("I have Olong tea")
...     
>>> varities.append("Oolong")
>>> varities
['Black', 'green', 'Masala', 'White', 'Oolong']
>>> if "Oolong" in varities:
...     print("I have Olong tea")
>>> squared_num = [x**2 for x in range(10)]
>>> squared_num
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube
Traceback (most recent call last):
  File "<python-input-61>", line 1, in <module>
    cube
NameError: name 'cube' is not defined
>>> cube_num = [y**3 for y in range(10)]
>>> cube_num
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> 
























