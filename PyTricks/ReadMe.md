## PyTricks

Предыдущая версия Вики -- [здесь](https://github.com/Nejel/coursera-python-specialization-repository/wiki)

Советы, трюки, идиомы -- [статья на proglib](https://proglib.io/p/python-tips-tricks/)

[Yields](https://habr.com/post/132554/)

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

zip возвращает последовательность кортежей 
[Больше про zip](https://www.programiz.com/python-programming/methods/built-in/zip)

```python
coordinate = ['x', 'y', 'z']
value = [3, 4, 5, 0, 9]

result = zip(coordinate, value)
resultList = list(result)
print(resultList)

c, v =  zip(*resultList)
print('c =', c)
print('v =', v)

>>>[('x', 3), ('y', 4), ('z', 5)]
>>>c = ('x', 'y', 'z')
>>>v = (3, 4, 5)
```

Enumerator возвращает нумерованный список от последовательности элементов

```python
x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))

>>>[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
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

```python

# Быстро выбрать нужные строки

for line in fh:
    if not line.startswith('From ') : continue # skip code
    words = line.split()
    email = words[1]
    lst.append(email)
    count += 1

```


```python

# Быстро читаем файлы (2 способа)
#Way 1
fname = input("Enter file name: ")
fh = open(fname, 'r')



#Way2
myfile = open('sample.txt') #this is class '_io.TextIOWrapper'
# dir(myfile) # way to look at available methods
content = myfile.read()
myfile.close()
print(content)


```
