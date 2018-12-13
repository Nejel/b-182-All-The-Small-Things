REGULAR EXPRESSIONS

* [Статья на Тпрогере](https://tproger.ru/translations/regular-expression-python/)
* [Документация к третьему Питону](https://docs.python.org/3/howto/regex.html)
* [Модификация строк при помощи re](https://docs.python.org/3/howto/regex.html#modifying-strings)
* [Поиск и замена](https://docs.python.org/3/howto/regex.html#search-and-replace)
* [Токенайзер (scanner analyzes)](https://docs.python.org/3/library/re.html#writing-a-tokenizer)


```
\d -- Matches any decimal digit;
this is equivalent to the class [0-9].

\D -- Matches any non-digit character;
this is equivalent to the class [^0-9].

\s -- Matches any whitespace character (вертикальные пробелы, межстрочные разделители);
this is equivalent to the class [ \t\n\r\f\v].

\S -- Matches any non-whitespace character;
this is equivalent to the class [^ \t\n\r\f\v].

\w -- Matches any alphanumeric character;
this is equivalent to the class [a-zA-Z0-9_].

\W -- Matches any non-alphanumeric character;
this is equivalent to the class [^a-zA-Z0-9_]
```


### Примеры

- [^5] will match any character except '5'
- For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'.
- . -- matches anything except a newline character
- \* -- (звездочка) предыдущий символ повторяется любое количество раз
- Let’s consider the expression a[bcd]*b. This matches the letter 'a',
zero or more letters from the class [bcd],
and finally ends with a 'b'. Now imagine matching this RE against the string 'abcbd'.
- The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional.
For example, home-?brew matches either 'homebrew' or 'home-brew'.



### Методы

* re.match()
* re.search()
* re.findall()
* re.split()
* [re.sub()](https://docs.python.org/3/library/re.html#re.sub) - замена
re.compile()


```python
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
```
