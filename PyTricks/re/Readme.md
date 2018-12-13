REGULAR EXPRESSIONS

[Статья на Тпрогере](https://tproger.ru/translations/regular-expression-python/)
[Документация к третьему Питону](https://docs.python.org/3/howto/regex.html)



```python
\d
Matches any decimal digit; this is equivalent to the class [0-9].
\D
Matches any non-digit character; this is equivalent to the class [^0-9].
\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_]
```


```
re.match()
re.search()
re.findall()
re.split()
re.sub()
re.compile()

import re
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print result

Результат:
<_sre.SRE_Match object at 0x0000000009BE4370>
```


```
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
```