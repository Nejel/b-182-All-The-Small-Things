## PyTricks 

Предыдущая версия Вики -- [здесь](https://github.com/Nejel/coursera-python-specialization-repository/wiki)

Советы, трюки, идиомы -- [статья на proglib](https://proglib.io/p/python-tips-tricks/)

[Идиомы](http://safehammad.com/downloads/python-idioms-2014-01-16.pdf): 

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


```python

#Build lists using list comprehensions

# GOOD
data = [7, 20, 3, 15, 11]
result = [i * 3 for i in data if i > 10]
print(result) # [60, 45, 33]

# NOT SO GOOD (MOST OF THE TIME)
data = [7, 20, 3, 15, 11]
result = []
for i in data:
if i > 10:
result.append(i * 3)
print(result) # [60, 45, 33]

```


```python
# Create dict from keys and values using zip

# GOOD
keys = ['Safe', 'Bob', 'Thomas']
values = ['Hammad', 'Builder', 'Engine']
d = dict(zip(keys, values))
print(d) # {'Bob': 'Builder',
'Safe': 'Hammad',
'Thomas': 'Engine'}


# NOT SO GOOD
keys = ['Safe', 'Bob', 'Thomas']
values = ['Hammad', 'Builder', 'Engine']
d = {}
for i, key in enumerate(keys):
d[keys] = values[i]
print(d) # {'Bob': 'Builder',
'Safe': 'Hammad',
'Thomas': 'Engine'}

```



