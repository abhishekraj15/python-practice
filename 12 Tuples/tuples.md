>>> item_types = ("Black", "Green", "Oolong")
>>> item_types
('Black', 'Green', 'Oolong')
>>> item_types[0]
'Black'
>>> item_types[-1]
'Oolong'
>>> item_types[1:]
('Green', 'Oolong')
>>> 




















# New Feature
item_types[0] = "Lemon Tea"
Traceback (most recent call last):
  File "<python-input-5>", line 1, in <module>
    item_types[0] = "Lemon Tea"
    ~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
>>> 


>>> len(item_types)
3
>>> more_items = ("Herbal", "Earl Gray")
>>> all_items = more_items + item_types
>>> all_items
('Herbal', 'Earl Gray', 'Black', 'Green', 'Oolong')
>>> if "Green" in all_items
  File "<python-input-11>", line 1
    if "Green" in all_items
                           ^
SyntaxError: expected ':'
>>> if "Green" in all_items:
...     print("I have green item")
...     
I have green item
>>> more_item = ("Herbal", "Earl Grey", "Herbal")
>>> more_item
('Herbal', 'Earl Grey', 'Herbal')
>>> more_item.count("Hrebal")
0
>>> more_item.count("Herbal")
2
>>> item_types
('Black', 'Green', 'Oolong')
>>> (black, green, Oolong) = item_types
>>> black
'Black'
>>> green
'Green'
>>> Oolang
Traceback (most recent call last):
  File "<python-input-21>", line 1, in <module>
    Oolang
NameError: name 'Oolang' is not defined. Did you mean: 'Oolong'?
>>> Oolong
'Oolong'
>>> type(item_types)
<class 'tuple'>
>>> ("", (1, 2, 3), "")
('', (1, 2, 3), '')
>>> 