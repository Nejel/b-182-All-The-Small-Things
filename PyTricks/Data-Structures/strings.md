Don’t do this:

```python

s = ''
for x in l:
    # this makes a new string every iteration, because strings are immutable
    s += x
    
```
    
Instead:

```python
# ...
# l.append(x)
s = ''.join(l)

```

You can even use generator expressions, which are extremely efficient:

```python
s = ''.join(f(x) for x in l)
```

If you do want a mutable string-like object, you can use StringIO.
