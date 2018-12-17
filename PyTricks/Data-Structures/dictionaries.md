To iterate through a dictionary, either keys, values, or both:

```python

# Iterate over keys
for k in d:
    ...

# Iterate over values, Python 3
for v in d.values():
    ...

# Iterate over values, Python 2
# In Python 2, dict.values() returns a copy
for v in d.itervalues():
    ...

# Iterate over keys and values, Python 3
for k, v in d.items():
    ...

```


```python
# Iterate over values, Python 2
# In Python 2, dict.items() returns a copy
for k, v in d.iteritems():
    ...
```


Anti-patterns:

```python

for k, _ in d.items():  # instead: for k in d:
    ...
for _, v in d.items():  # instead: for v in d.values()
    ...

```


FIXME:

setdefault
usually better to use collections.defaultdict
dict.get is useful, but using dict.get and then checking if it is None as a way of testing if the key is in the dictionary is an anti-idiom, as None is a potential value, and whether the key is in the dictionary can be checked directly. It’s ok to use get and compare with None if this is not a potential value, however.

Simple:

```python
if 'k' in d:
    # ... d['k']
Anti-idiom (unless None is not a potential value):

v = d.get('k')
if v is not None:
    # ... v

```

Dict from parallel sequences of keys and values
Use zip as: dict(zip(keys, values))

