Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> our_tuple = 1,2,"A","B","C"
>>> type(our_tuple)
<class 'tuple'>
>>> our_tuple = (1,2,"A","B","C")
>>> type(our_tuple)
<class 'tuple'>
>>> our_tuple[0:3]
(1, 2, 'A')
>>> our_list = [0,1,2,3,4,5,6]
>>> our_list[2] =100
>>> our_list
[0, 1, 100, 3, 4, 5, 6]
>>> our_tuple = (1,2,"A","B","C")
>>> our_tuple[2] = 100
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    our_tuple[2] = 100
TypeError: 'tuple' object does not support item assignment
>>> A = [1,2,3]
>>> tuple(A)
(1, 2, 3)
>>> A
[1, 2, 3]
>>> A = tuple(A)
>>> A
(1, 2, 3)
>>> (A,B,C) = 1,2,3
>>> A
1
>>> B
2
>>> C
3
>>> (A,B,C) = (1,2,3)
>>> B
2
>>> D,E,F = [1,2,3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> D,E,F = [1,2,3]
>>> E
2
>>> G,H,I = "425"
>>> H
'2'
>>> G
'4'
>>> 