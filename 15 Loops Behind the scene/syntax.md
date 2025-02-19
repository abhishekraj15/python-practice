> > > f = open('item.py')
> > > f.readline()
> > > 'print("Item is here")\n'
> > > f.readline()
> > > '\n'
> > > f.readline()
> > > 'username = "abhishek"\n'
> > > f.readline()
> > > 'print(username)'
> > > f.readline()
> > > ''

> > > f = open('item.py')
> > > f.**next**()
> > > 'print("Item is here")\n'
> > > f.**next**()
> > > '\n'
> > > f.**next**()
> > > 'username = "abhishek"\n'
> > > f.**next**()
> > > 'print(username)\n'
> > >
> > > f.**next**()
> > > '\n'
> > > f.**next**()
> > > '\n'
> > > f.**next**()
> > > Traceback (most recent call last):
> > > File "<python-input-15>", line 1, in <module>

    f.__next__()
    ~~~~~~~~~~^^

StopIteration

> > >

> > > f = open('item.py')
> > > for line in open('item.py'):
> > > ... print(line)
> > > ...  
> > > print("Item is here")

username = "abhishek"

print(username)

> > >

> > > f = open('item.py')
> > > for line in open('item.py'):
> > > ... print(line)
> > > ...  
> > > print("Item is here")

> > > f = open('item.py')
> > > while True:
> > > ... line = f.readline()
> > > ... if not line: break
> > > ... print(line, end='')
> > > ...  
> > > print("Item is here")

username = "abhishek"
print(username)

> > >

> > > f = open('item.py')
> > > for line in open('item.py'):
> > > ... print(line)
> > > ...  
> > > print("Item is here")

> > > test = "hitesh"
> > > if not test:
> > > ... print("hello")
> > > ...  
> > > test = ""
> > > if not test:
> > > ... print("Hello")
> > > ...  
> > > Hello

> > > f = open('item.py')
> > > for line in open('item.py'):
> > > ... print(line)
> > > ...  
> > > print("Item is here")

> > > mtList = [1, 2, 3, 4]
> > > I = iter(myList)
> > > Traceback (most recent call last):
> > > File "<python-input-25>", line 1, in <module>

    I = iter(myList)
             ^^^^^^

NameError: name 'myList' is not defined. Did you mean: 'mtList'?

> > > I = iter(mtList)
> > > I
> > > <list_iterator object at 0x104eb16f0>
> > > I.**next**()
> > > 1
> > > I
> > > <list_iterator object at 0x104eb16f0>
> > > I.**next**()
> > > 2
> > > I.**next**()
> > > 3
> > > I.**next**()
> > > 4
> > > I.**next**()
> > > Traceback (most recent call last):
> > > File "<python-input-33>", line 1, in <module>

    I.__next__()
    ~~~~~~~~~~^^

StopIteration

> > >

> > > f = open('item.py')
> > > for line in open('item.py'):
> > > ... print(line)
> > > ...  
> > > print("Item is here")

> > > mtList = [1, 2, 3, 4]
> > > I = iter(myList)
> > > Traceback (most recent call last):
> > > File "<python-input-25>", line 1, in <module>

    I = iter(myList)
             ^^^^^^

NameError: name 'myList' is not defined. Did you mean: 'mtList'?

> > > f = open('item.py')
> > > iter(f) is f
> > > True
> > > iter(f) is f.**iter**()
> > > True

> > > f = open('item.py')
> > > for line in open('item.py'):
> > > ... print(line)
> > > ...  
> > > print("Item is here")

> > > mtList = [1, 2, 3, 4]
> > > I = iter(myList)
> > > Traceback (most recent call last):
> > > File "<python-input-25>", line 1, in <module>

    I = iter(myList)
             ^^^^^^

NameError: name 'myList' is not defined. Did you mean: 'mtList'?

> > > myNewList = [1, 2, 3]
> > > iter(myNewList) is myNewList
> > > False




>>> f = open('item.py')
>>> for line in open('item.py'):
...     print(line)
...     
print("Item is here")

>>> mtList = [1, 2, 3, 4]
>>> I = iter(myList)
Traceback (most recent call last):
  File "<python-input-25>", line 1, in <module>
    I = iter(myList)
             ^^^^^^
NameError: name 'myList' is not defined. Did you mean: 'mtList'?
>>> D = {'a': 1, 'b': 2}
>>> for key in D.keys():
...     print(key)
...     
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x10505d800>
>>> nex(I)
Traceback (most recent call last):
  File "<python-input-43>", line 1, in <module>
    nex(I)
    ^^^
NameError: name 'nex' is not defined. Did you mean: 'hex'?
>>> next(I)
'a'
>>> 
>>> next(I)
'b'
>>> 
>>> next(I)
Traceback (most recent call last):
  File "<python-input-48>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> 



>>> f = open('item.py')
>>> for line in open('item.py'):
...     print(line)
...     
print("Item is here")

>>> mtList = [1, 2, 3, 4]
>>> I = iter(myList)
Traceback (most recent call last):
  File "<python-input-25>", line 1, in <module>
    I = iter(myList)
             ^^^^^^
NameError: name 'myList' is not defined. Did you mean: 'mtList'?
>>> D = {'a': 1, 'b': 2}
>>> for key in D.keys():
...     print(key)
...     
a
b
>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x10505d800>
>>> nex(I)
Traceback (most recent call last):
  File "<python-input-43>", line 1, in <module>
    nex(I)
    ^^^
NameError: name 'nex' is not defined. Did you mean: 'hex'?
>>> next(I)
'a'
>>> 
>>> next(I)
>>> range(0, 5)
range(0, 5)
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)
>>> next(I)
0
>>> next(I)
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<python-input-58>", line 1, in <module>
    next(I)
    ~~~~^^^
StopIteration
>>> 