REGULAR EXPRESSIONS

* [Статья на Тпрогере](https://tproger.ru/translations/regular-expression-python/)
* [Документация к третьему Питону](https://docs.python.org/3/howto/regex.html)
* [Модификация строк при помощи re](https://docs.python.org/3/howto/regex.html#modifying-strings)
* [Поиск и замена](https://docs.python.org/3/howto/regex.html#search-and-replace)
* [Токенайзер (scanner analyzes)](https://docs.python.org/3/library/re.html#writing-a-tokenizer)
* [Lookahead assertions (проверка впередистоящих значений на соответствие)](https://docs.python.org/3/howto/regex.html#lookahead-assertions)
* [Modifying and splitting Strings](https://docs.python.org/3/howto/regex.html#modifying-strings)
* [Search and replace (sub)](https://docs.python.org/3/howto/regex.html#search-and-replace)
* [Статья Гриши Петрова на Хабре](https://habr.com/post/60369/)
* [Интерактивная демка (ссылка источник, сама демка также есть в этом репо)](https://github.com/python/cpython/blob/3.7/Tools/demo/redemo.py)


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

### Короткая справка

- [^5] will match any character except '5'
- For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'.
- . -- matches anything except a newline character
- + -- one or more repetitions
- \* -- (звездочка) предыдущий символ повторяется любое количество раз
- Let’s consider the expression a[bcd]*b. This matches the letter 'a',
zero or more letters from the class [bcd],
and finally ends with a 'b'. Now imagine matching this RE against the string 'abcbd'.
- The question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional.
For example, home-?brew matches either 'homebrew' or 'home-brew'.
- {1,3} -- This qualifier means there must be at least m repetitions, and at most n. For example, a/{1,3}b will match 'a/b', 'a//b', and 'a///b'. It won’t match 'ab', which has no slashes, or 'a////b', which has four.
- {1,} -- one repetition+
- ^ -- Matches at the beginning of lines.
- | -- Alternation, or the “or” operator.
- $ -- Matches at the end of a line, which is defined as either the end of the string, or any location followed by a newline character.
- \A -- Matches only at the start of the string.
- \Z -- Matches only at the end of the string.
- \b -- Word boundary. That matches only at the beginning or end of a word.
- \B -- Another zero-width assertion, this is the opposite of \b, only matching when the current position is not at a word boundary.


### Методы

|Method/Attribute| Purpose  |   
|---|
| match()  |  Determine if the RE matches at the beginning of the string. |   
|  search() |  Scan through a string, looking for any location where this RE matches |   
| findall()  |  Find all substrings where the RE matches, and returns them as a list. |  
| finditer()  | Find all substrings where the RE matches, and returns them as an iterator.  |
| group()| 	Return the string matched by the RE
| start()| 	Return the starting position of the match
| end()| 	Return the ending position of the match
| span()| 	Return a tuple containing the (start, end) positions of the match


* re.match()
* re.search()
* re.findall()
* re.split()
* [re.sub()](https://docs.python.org/3/library/re.html#re.sub) - замена
re.compile()


### [Grouping](https://docs.python.org/3/howto/regex.html#grouping)

Groups are marked by the '(', ')' metacharacters. '(' and ')' have much the same meaning as they do in mathematical expressions; they group together the expressions contained inside them, and you can repeat the contents of a group with a repeating qualifier, such as *, +, ?, or {m,n}. For example, (ab)* will match zero or more repetitions of ab.

```python
>>> p = re.compile('(ab)*')
>>> print(p.match('ababababab').span())
(0, 10)
```

Groups are numbered starting with 0. Group 0 is always present; it’s the whole RE, so match object methods all have group 0 as their default argument.

```python
>>> p = re.compile('(a)b')
>>> m = p.match('ab')
>>> m.group()
'ab'
>>> m.group(0)
'ab'
```


```python

>>> p = re.compile('(a(b)c)d')
>>> m = p.match('abcd')
>>> m.group(0)
'abcd'
>>> m.group(1)
'abc'
>>> m.group(2)
'b'

>>> m.group(2,1,2)
('b', 'abc', 'b')

>>> m.groups()
('abc', 'b')
```

```python
>>> p = re.compile(r'(?P<word>\b\w+\b)')
>>> m = p.search( '(((( Lots of punctuation )))' )
>>> m.group('word')
'Lots'
>>> m.group(1)
'Lots'
```


```python
# Grouping date

InternalDate = re.compile(r'INTERNALDATE "'
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
        r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        r'"')
```



### The R prefix

The r prefix, making the literal a raw string literal, is needed in this example because escape sequences in a normal “cooked” string literal that are not recognized by Python, as opposed to regular expressions, now result in a DeprecationWarning and will eventually become a SyntaxError. See The [Backslash Plague](https://docs.python.org/3/howto/regex.html#the-backslash-plague).

### [Compilation flags](https://docs.python.org/3/howto/regex.html#compilation-flags)

| Flag| 	Meaning |
|---| |
| ASCII, A |	Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property. |
|DOTALL, S |	Make . match any character, including newlines.
|IGNORECASE, I | 	Do case-insensitive matches.
|LOCALE, L | 	Do a locale-aware match.
|MULTILINE, M | 	Multi-line matching, affecting ^ and $.
|VERBOSE, X (for ‘extended’) | 	Enable verbose REs, which can be organized more cleanly and understandably.

#### Verbose

This flag allows you to write regular expressions that are more readable by granting you more flexibility in how you can format them. When this flag has been specified, whitespace within the RE string is ignored, except when the whitespace is in a character class or preceded by an unescaped backslash; this lets you organize and indent the RE more clearly. This flag also lets you put comments within a RE that will be ignored by the engine; comments are marked by a '#' that’s neither in a character class or preceded by an unescaped backslash.

With Verbose:
```python
charref = re.compile(r"""
 &[#]                # Start of a numeric entity reference
 (
     0[0-7]+         # Octal form
   | [0-9]+          # Decimal form
   | x[0-9a-fA-F]+   # Hexadecimal form
 )
 ;                   # Trailing semicolon
""", re.VERBOSE)
```

Without Verbose:
```python
charref = re.compile("&#(0[0-7]+"
                     "|[0-9]+"
                     "|x[0-9a-fA-F]+);")
```

In the above example, Python’s automatic concatenation of string literals has been used to break up the RE into smaller pieces, but it’s still more difficult to understand than the version using re.VERBOSE.



### Примеры

```python
>>> m.group()
'tempo'
>>> m.start(), m.end()
(0, 5)
>>> m.span()
(0, 5)
```

```python
str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print 'found', match.group() ## 'found word:cat'
else:
  print 'did not find'
```


```python
## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') =>  found, match.group() == "iii"
match = re.search(r'igs', 'piiig') =>  not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig') =>  found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') =>  found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') =>  found, match.group() == "abc"
```


```python
p = re.compile( ... )
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
```

```python
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
```


```python
>>> p = re.compile(r'\d+')
>>> p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
['12', '11', '10']
```


Detects doubled words in a string:

```python
>>> p = re.compile(r'\b(\w+)\s+\1\b')
>>> p.search('Paris in the the spring').group()
'the the'
```


Пример ниже возвращает список объектов типа 'результат поиска'. Получая эти загадочные объекты вместо обычных строк (которые может вернуть, к примеру, метод findall), мы получаем возможность не только ознакомиться с фактом что текст найден, но и узнать где именно он найден — для этого у объекта типа 'результат поиска' есть специально обученный метод span(), возвращающий точное положение найденного фрагмента в исходном тексте.

```python
result = re.finditer( ur"{[^}\n]+}", txt )
for match in result :
  print match.group()
```


В примере ниже в регулярке выделены три группы: "({[^}\n]+})" соответствует заголовку в фигурных скобках,
"([^=\n]+)" перед знаком '=' соответствует имени поля и "([^\n]+)" после знака '=' соответствует значению поля. При этом также используется странная группа "(?:)", которая объединяет группы имен и значений полей. Это специальная группа для использования с логическим оператором '|' — она позволяет объединять несколько групп одним оператором '|' без побочных эффектов. Во-вторых, для распечатки результатов использован метод groups() вместо метода group(). Это не спроста — библиотека регулярных выражений в питоне имеет свое собственное представление о том, что такое «результат поиска». Выражается эта самостийность в том, что регулярное выражение из двух групп "([^=\n]+)=([^=\n]+)", примененное к тесту «a=b» вернет ОДИН объект типа «результат», который состоит из нескольких ГРУПП.

```python
result = re.finditer( ur"({[^}\n]+})|(?:([^=\n]+)=([^\n]+))", txt )
for match in result :
  print match.groups()

```


```python
import re
txt = '''
{number section}
num=1
{text section}
txt="2"
'''
object = re.compile( ur"(?P<section>{[^}\n]+})|(?:(?P<name>[^=\n]+)=(?P<value>[^\n]+))", re.M | re.S | re.U )
#Перед поиском используется метод re.compile(), который возвращает
# так называемое «скомпилированное регулярное выражение».
# Кроме скорости работы и удобства у него есть одно замечательное свойство —
# если вызвать его метод groupindex(), то мы получим словарь,
# содержащий имена всех найденных групп и из индексы.
# К сожалению, словарь почему-то инвертирован — кючем в нем является не индекс, а имя группы.

# используются флаги re.M (корректный поиск начала строки "^" и конца строки "$" в многостроковом тексте), re.S ("." находит совсем все, включая \n) и .U (корректный поиск в unicode тексте)

result = object.finditer( txt )
group_name_by_index = dict( [ (v, k) for k, v in object.groupindex.items() ] )
# можно использовать для получения имени группы по ее номеру

print group_name_by_index
for match in result :
  for group_index, group in enumerate( match.groups() ) :
    if group :
      print "text: %s" % group
      print "group: %s" % group_name_by_index[ group_index + 1 ]
      print "position: %d, %d" % match.span( group_index + 1 )

# В результате разбор найденного занимает два цикла —
# сначала мы итерируемся по результатам поиска, а затем для каждого результата
# по содержащимся в нем группам. Результатом является точный и полный список токенов,
# с указанием их типа и позиции в тексте.
# Этот список можно использовать для обработки текста, подсветки синтаксиса,
# нахождения ошибок — в общем штука нужная и полезная.

```
