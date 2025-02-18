# Python Dictionary

>>> item_types = { "Masala": "Spicy", "Ginger": "Zesty"}
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> item_types = { "Masala": "Spicy", "Ginger": "Zesty", "Green":"Tasty"}
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Tasty'}
>>> 


# Items Acces In Dictionary

item_types["Masala"]
'Spicy'
>>> item_types.get("Ginger")
'Zesty'
>>> item_types("Gingery")
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    item_types("Gingery")
    ~~~~~~~~~~^^^^^^^^^^^
TypeError: 'dict' object is not callable
>>> item_types.get("Gingery")

# Items Change in DIctionary

>>> item_types = { "Masala": "Spicy", "Ginger": "Zesty"}
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Tasty'}
>>> item_types["Green"] = "Fresh"
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> 

# Iteration In Dictionary

>>> item_types = { "Masala": "Spicy", "Ginger": "Zesty"}
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> for taste in item_types:
...     print(taste)
...     
Masala
Ginger
Green
>>> for taste in item_types:
...     print(taste,item_types[chai])
...     
Traceback (most recent call last):
  File "<python-input-13>", line 2, in <module>
    print(taste,item_types[chai])
                           ^^^^
NameError: name 'chai' is not defined
>>> for taste in item_types:
...     print(taste,item_types[taste])
...     
Masala Spicy
Ginger Zesty
Green Fresh
>>> for taste in item_types:
...     print(taste,item_types[taste])
...     
Masala Spicy
Ginger Zesty
Green Fresh
>>> for key, value in item_types.items():
...     print(key, value)
...     
Masala Spicy
Ginger Zesty
Green Fresh
>>> 
>>> 
>>> 
>>> 
>>> if "Masala" in item_types:
...     print("I have Masala")
...     
I have Masala
>>> print(len(item_types))
3
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Green': 'Fresh'}
>>> 




abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> item_types = { "Masala": "Spicy", "Ginger": "Zesty"}
>>> item_types["Earl Grey"] = "Citrus"
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Earl Grey': 'Citrus'}
>>> item_types.pop("Ginger")
'Zesty'
>>> item_types
{'Masala': 'Spicy', 'Earl Grey': 'Citrus'}
>>> item_types.popitem()
('Earl Grey', 'Citrus')
>>> item_types
{'Masala': 'Spicy'}
>>> item_types["Green": "Fresh"]
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    item_types["Green": "Fresh"]
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^
KeyError: slice('Green', 'Fresh', None)
>>> item_types["Green"]: "Fresh"
>>> item_types
{'Masala': 'Spicy'}
>>> item_types["Green"]= "Fresh"
>>> item_types
{'Masala': 'Spicy', 'Green': 'Fresh'}
>>> del item_types["Green"]
>>> item_types
{'Masala': 'Spicy'}
>>> item_types_copy = item_types.copy()
>>> item_shop = {
... "item1": {"Masala":"Spicy", "Ginger":"Zesty"}, 
... "item2":{"Green": "Mild" , "Black": "Strong"}
... }
>>> item_shop
{'item1': {'Masala': 'Spicy', 'Ginger': 'Zesty'}, 'item2': {'Green': 'Mild', 'Black': 'Strong'}}
>>> item_shop["item1"]
{'Masala': 'Spicy', 'Ginger': 'Zesty'}
>>> item_shop["item1"]["Ginger"]
'Zesty'
>>> 




abhishekrajput@Abhisheks-MacBook-Air Python % python3
Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> item_types = { "Masala": "Spicy", "Ginger": "Zesty"}
>>> item_types["Earl Grey"] = "Citrus"
>>> item_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'Earl Grey': 'Citrus'}
>>> item_types.pop("Ginger")
'Zesty'
>>> item_types
{'Masala': 'Spicy', 'Earl Grey': 'Citrus'}
>>> item_types.popitem()
('Earl Grey', 'Citrus')
>>> item_types
{'Masala': 'Spicy'}
>>> item_types["Green": "Fresh"]
>>> squared_num = {x: x**2 for x in range(6)}
>>> squared_num
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> squared_num.clear()
>>> squared_num
{}
>>> 
>>> 
>>> 
>>> keys = ["Masala", "Ginger", "Lemon"]
>>> keys
['Masala', 'Ginger', 'Lemon']
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'Masala': 'Delicious', 'Ginger': 'Delicious', 'Lemon': 'Delicious'}
>>> new_dict = dict.fromkeys(keys, keys)
>>> new_dict
{'Masala': ['Masala', 'Ginger', 'Lemon'], 'Ginger': ['Masala', 'Ginger', 'Lemon'], 'Lemon': ['Masala', 'Ginger', 'Lemon']}
>>> 













































