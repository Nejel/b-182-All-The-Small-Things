## PyTricks. Collections

Предыдущая версия Вики -- [здесь](https://github.com/Nejel/coursera-python-specialization-repository/wiki)

Python поставляется с модулем, который содержит несколько контейнеров из типов данных, называемых коллекциями. Сначала я хотел рассказать только о двух из них, но на данный момент их уже более трех и называются они namedtuple(), deque(связный список), и OrderedDict.


```python
# defaultdict
#Этот тип пригодится, когда вы добавляете списки внутри словаря. Если вы используете dict(),то вам нужно будет проверить, существует ли ключ до добавления, но с defaultdict этого делать не нужно. Например.


from collections import defaultdict

order = (
    ('Mark', 'Steak'),
    ('Andrew', 'Veggie Burger'),
    ('James', 'Steak'),
    ('Mark', 'Beer'),
    ('Andrew', 'Beer'),
    ('James', 'Wine'),
)

group_order = defaultdict(list)

for name, menu_item in order:
    group_order[name].append(menu_item)

print group_order

# вывод
# defaultdict(, {
#     'James': ['Steak', 'Wine'],
#     'Andrew': ['Veggie Burger', 'Beer'],
#     'Mark': ['Steak', 'Beer']
# })
	
```

Мы могли бы также считать их вот так.

```python

order_count = defaultdict(int)

for name, menu_item in order:
    order_count[menu_item] += 1

print order_count

# вывод
# defaultdict(, {
#     'Beer': 2, 
#     'Steak': 2, 
#     'Wine': 1, 
#     'Veggie Burger': 1
# })
	
```
	
	
## PyTricks. Counter


Может, последний пример будет лишним, так как коллекции уже содержат класс, называемый Counter. В этом случае мне нужно сначала извлечь второй элемент из каждого tuple, для которого я могу использовать выражение генератора.

```python

from collections import Counter

order_count =  Counter(menu_item for name, menu_item in order)
print order_count

# вывод
# Counter({
#    'Beer': 2,
#    'Steak': 2,
#    'Wine': 1,
#    'Veggie Burger': 1
# })
		
```
	
Другой, может быть, лучший, пример может посчитать все уникальные строки, которые появляются в файле. Это делается очень просто.

```python

with open('/some/file', 'r') as f:
    line_count = Counter(f)
	
```

