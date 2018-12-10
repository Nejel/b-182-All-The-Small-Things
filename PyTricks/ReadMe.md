## PyTricks 

Предыдущая версия Вики -- [здесь](https://github.com/Nejel/coursera-python-specialization-repository/wiki)

Советы, трюки, идиомы -- [статья на proglib](https://proglib.io/p/python-tips-tricks/)

Идиомы: 

```python

#if x in items
#for x in items

#Example (contains)
name = 'Safe Hammad'
if 'H' in name:
print('This name has an H in it!')


#Example (iteration)
pets = ['Dog', 'Cat', 'Hamster']
for pet in pets:
print('A', pet, 'can be very cute!')

```


```python

#if | if not 

{'Safe': 'Cat', 'George': 'Dog'}
if name and pets and owners:
print('We have pets!')

```


```python

# быстрое переназначение переменных

a, b = b, a


a, b = 5, 6
print(a, b) # 5, 6
a, b = b, a
print(a, b) # 6, 5

```


```python

 # Создание стринги из последовательности 
 
 chars = ['S', 'a', 'f', 'e']
 name = ''.join(chars)
 print(name) # Safe

```

```python

 # Создание стринги из последовательности 
 
 chars = ['S', 'a', 'f', 'e']
 name = ''.join(chars)
 print(name) # Safe

```


```python

# try except 

d = {'x': '5'}
try:
value = int(d['x'])
except (KeyError, TypeError, ValueError):
value = None

```

