Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> students = {}
>>> stundets = {"Alice":25,"Bob":27,"Claire":17,"Dan":21,"Emma":22}
>>> students = {"Alice":25,"Bob":27,"Claire":17,"Dan":21,"Emma":22}
>>> students["Dan"]
21
>>> students["Fred"]=25
>>> students["Fred]
	 
SyntaxError: EOL while scanning string literal
>>> 
>>> students["Fred"]
25
>>> students["Alice"]
25
>>> students["Alice"]=26
>>> students["Alice"]
26
>>> del students["Fred"]
>>> students["Fred"]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    students["Fred"]
KeyError: 'Fred'
>>> studnets.keys()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    studnets.keys()
NameError: name 'studnets' is not defined
>>> students.keys()
dict_keys(['Alice', 'Bob', 'Claire', 'Dan', 'Emma'])
>>> students.keys()[0]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    students.keys()[0]
TypeError: 'dict_keys' object is not subscriptable
>>> a=list(students.keys())
>>> a
['Alice', 'Bob', 'Claire', 'Dan', 'Emma']
>>> ap0]
SyntaxError: unmatched ']'
>>> a[0]
'Alice'
>>> a[3]
'Dan'
>>> students.values()
dict_values([26, 27, 17, 21, 22])
>>> list(students.values())[2:]
[17, 21, 22]
>>> students.values()[2:]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    students.values()[2:]
TypeError: 'dict_values' object is not subscriptable
>>> print(students)
{'Alice': 26, 'Bob': 27, 'Claire': 17, 'Dan': 21, 'Emma': 22}
>>> students.values()[0]
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    students.values()[0]
TypeError: 'dict_values' object is not subscriptable
>>> print(students)
{'Alice': 26, 'Bob': 27, 'Claire': 17, 'Dan': 21, 'Emma': 22}
>>> 