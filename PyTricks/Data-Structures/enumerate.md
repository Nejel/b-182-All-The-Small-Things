## PyTricks 

Предыдущая версия Вики -- [здесь](https://github.com/Nejel/coursera-python-specialization-repository/wiki)

Достаточно распространенная вещь — это цикл в списке, который также отслеживает индекс текущего элемента. Мы можем использовать переменную count, но python дает нам лучший синтаксис для этого в качестве функции enumerate().

```python
 
students = ('James', 'Andrew', 'Mark')
for i, student in enumerate(students):
    print i, student
	
# вывод:
# 0 James
# 1 Andrew
# 2 Mark 
	
```