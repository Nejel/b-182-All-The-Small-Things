## PyTricks

Предыдущая версия Вики -- [здесь](https://github.com/Nejel/coursera-python-specialization-repository/wiki)

[Идиомы на Python Programming wiki](https://en.wikibooks.org/wiki/Python_Programming/Idioms)

[Idioms and Anti-Idioms in Python (Python2)](https://docs.python.org/2/howto/doanddont.html)

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


Посчитать количество элементов в словаре
```python

n = 10
ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

def sockMerchant(n, ar):
    MyList = ar
    my_dict = {i:MyList.count(i) for i in MyList} # Посчитать количество элементов в словаре. {1: 4, 3: 5, 2: 1} 1 (встречается 4 раза), 3 (5 раз)
    print(my_dict) # {1: 4, 3: 5, 2: 1}
    result = 0
    for k, v in my_dict.items():
        #if v > 1:
        if v > 1 and v // 2:
            print(k) # считаем элементы, которые делятся нацело и встречаются больше 1 раза: 1 (встречается 4 раза), 3 (5 раз)
            result += (v // 2)
        else:
            pass

    return result


sockMerchant(n, ar)

```


Посчитать количество элементов в словаре (full version)
```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    MyList = ar
    my_dict = {i:MyList.count(i) for i in MyList}
    print(my_dict)
    result = 0
    for k, v in my_dict.items():
        #if v > 1:
        if v > 1 and v // 2:
            print(k)
            result += (v // 2)
        else:
            pass

    return result


if __name__ == '__main__':
    #fptr = open(os.environ['1.txt'], 'w')

    n = 10

    ar = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
```


Посчитать количество выходов в ниже нуля (считаем долины):
```python
def countingValleys(way):
    highcounter = 0
    abovesealevel = 'unknown'
    direction = 'unknown'
    valleycounter = 0
    stepsup = 0
    stepsdown = 0
    for i in way:
        if i == 'D':
            direction = 'Down'
            stepsdown += 1
            #if valleycounter == 0:
            #    valleycounter = 1
            highcounter -= 1
            if highcounter < 0:
                abovesealevel = 'No'



        if i == 'U':
            direction = 'Up'
            stepsup -= 1
            highcounter += 1
            if highcounter > 0:
                abovesealevel = 'Yes'
        else:
            pass

        if direction == 'Down' and highcounter == -1:
            valleycounter += 1

    return valleycounter


way = 'UDDDUDUU'
result = countingValleys(way)
print(result)
```


Считаем гласные
```python
def minion_game(string):
    # your code goes here
    result = 'fake'
    kevin = 0
    stuart = 0
    counter = 0

    for i in s:
        if i in ['A', 'E', 'I', 'O', 'U']:
            counter += 1
            kevin += (len(s) - (counter - 1))
        else:
            counter += 1
            stuart += (len(s) - (counter - 1))

    if kevin > stuart:
        result = ('Kevin %s' % kevin)
        print(result)
    elif kevin < stuart:
        result = ('Stuart %s' % stuart)
        print(result)
    else:
        print('Draw')
    return result


if __name__ == '__main__':
    s = input()
    minion_game(s)
```


Select next element in list
```python
li = [0, 1, 2, 3]
running = True
while running:
    for elem in li:
        thiselem = elem
        nextelem = li[li.index(elem)+1]
```


Перемножаем стринги и ищем конкретный элемент, считаем количество его повторений.
```python

def repeatedString(s, n):
    counter = 0
    if len(s) > 1:
        s1 = s[0]
        slong = s * n
        slong2 = slong[0:n]
        #print(slong2)
        for i in slong2:
            if i == s1:
                counter += 1
            else:
                pass
    else:
        counter = n
    return counter

```

Просто извлекаем элементы по номерам
```python
nd = input().split()
n = int(nd[0])
d = int(nd[1])
```


Удаляем первый элемент из листа и добавляем его в конец листа (Arrays: Left Rotation)
```python
def rotLeft(a, d):
    for i in range (0, d):
        a1 = a[0]
        del a[0]
        a.append(a1)
    return a
```


Сравнить два массива (array) и показать результат
```python

arr1 = [(7, 0.78, 7920), (8, 0.9, 9000)]
arr2 = [(7, 1.68, 8460)]

dict1 = {i: (x, y) for i, x, y in arr1}
dict2 = {i: (x, y) for i, x, y in arr2}

diffArray = [
    (
        i,
        abs(dict2[i][0] - dict1[i][0]),
        abs(dict2[i][1] - dict1[i][1]),
    )
    if i in dict2
    else (i, dict1[i][0], dict1[i][1])
    for i in dict1
]

print(diffArray)

# Surprising result hule
# [(7, 0.8999999999999999, 540), (8, 0.9, 9000)]

```


Преобразовать стрингу в лист и сравнить символы попарно
```python

#s = ['A','A','A','B','B','B']
s = 'AAABBB'

def alternatingCharacters(s):
    counter = 0
    s = [i for i in s]  # преобразуем стрингу в лист
    print(s)
    try:
        for elem in s:
            try:
                thiselem = elem  # текущий элемент
                nextelem = s[s.index(
                    elem) + 1]  # смотрим какой следующий элемент в списке. скорее всего эта строка не стабаывает в конце списка
            except:
                counter += 1

            if thiselem == nextelem:
                del s[s.index(elem)]  # удаляем текущий элемент
                counter += 1

            elif thiselem != nextelem:
                pass
            # elif nextelem == '': # почему-то не работает
            #    counter += 1
    except:
        pass
    print(counter)
    # print(s)
    return counter

alternatingCharacters(s)

```
