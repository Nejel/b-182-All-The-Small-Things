## PyTricks 

Предыдущая версия Вики -- [здесь](https://github.com/Nejel/coursera-python-specialization-repository/wiki)

set это небольшая, но полезная структура данных, которая похожа на список, но каждое значение в ней уникально. Есть несколько полезных операций, помимо создания списка уникальных элементов, которые мы можем с ней сделать. Например, позволяет попробовать несколько способов проверки списков ввода.

```python

colours = set(['red', 'green', 'blue', 'yellow', 'orange', 'black', 'white'])

# либо используйте новейший синтаксис для объявления списка.
input_values = {'red', 'black', 'pizza'}

# получаем список допустимых цветов
valid_values = input_values.intersection(colours)

print valid_values
# вывод set(['black', 'red'])

# получаем список недопустимых цветов
invalid_values = input_values.difference(colours)

print invalid_values
# вывод set(['pizza'])

# если что-то не так, выкидываем исключение
if not input_values.issubset(colours):
    raise ValueError("Invalid colour: " + ", ".join(input_values.difference(colours)))
	

	
```