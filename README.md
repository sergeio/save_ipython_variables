save-ipython-variables
======================

You use IPython.  It's pretty great.  But things happen!  Your computer
crashes, your IPython shell crashes (in theory), your computer runs out of
memory and the process becomes unreachable.  You can lose your whole session,
and potentially hours of work.

Sure, you can work out of a file, using `%edit` to keep your code on disk, but
the variables that can take hours to build up -- whether it's through querying
databases, scraping the web, or long-running algorithms -- can just vanish.

This is where this module comes into play: `save-ipython-variables` lets you do
just that -- save your global IPython variables to disk easily, and load them
back into the global namespace when you need them again, even in a whole new
IPython session.

Example Usage
-------------
```python
In [1]: from save_ipython_variables import load_all_variables, save_variable

In [2]: data = build_data_dictionary_from_db()

In [3]: save_variable('data', data)

In [4]: save_variable('number', 5)

In [5]: exit()
```
And now, in a new session:
```python
In [1]: from save_ipython_variables import load_all_variables, save_variable

In [2]: load_all_variables()
Loaded the following variables: ['data', 'number']

In [3]: if data:
   ...:     print 'Loaded Successfully!'
Loaded Successfully!
```
You can also choose to load select variables:
```python
In [1]: from save_ipython_variables import load_all_variables, save_variable

In [2]: load_all_variables(['number'])
Loaded the following variables: ['number']

In [3]: number
Out[3]: 5

In [3]: data
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-8-2cd6ee2c70b0> in <module>()
----> 1 data

NameError: name 'data' is not defined
```
As you can see, `number` was successfully loaded, but `data` was ignored.
