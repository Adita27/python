Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> L=[1,5,2,6,2,9]
>>> 2 in L
True
>>> 3 in L
False
>>> 
======== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py ========
8
Hi! My name is Travis
What is your name?: Adrian
name NOT reconised
Hi! My name is Travis
What is your name?: Dan
name reconised
Hi! My name is Travis
What is your name?: dan
name NOT reconised
Hi! My name is Travis
What is your name?: 
name NOT reconised
Hi! My name is Travis
What is your name?: 
name NOT reconised
Hi! My name is Travis
What is your name?: 
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/Python bible/travis.py", line 7, in <module>
    name = input("What is your name?: ").strip()
KeyboardInterrupt
>>> 
======== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py ========
8
Hi! My name is Travis
What is your name?: dan
name reconised
Hi! My name is Travis
What is your name?: 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
8
Hi! My name is Travis
What is your name?: Alice
Hello Alice!
Would you like to be remove from the system (y/n)?: y
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/Python bible/travis.py", line 14, in <module>
    known_users.remove(name) #elimina din lista numele
NameError: name 'known_users' is not defined
>>> 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
8
Hi! My name is Travis
What is your name?: Alice
Hello Alice!
Would you like to be remove from the system (y/n)?: y
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
['Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
Hi! My name is Travis
What is your name?: Alice
Hi! My name is Travis
What is your name?: Dan
Hello Dan!
Would you like to be remove from the system (y/n)?: n
name NOT reconised
Hi! My name is Travis
What is your name?: 
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/Python bible/travis.py", line 7, in <module>
    name = input("What is your name?: ").strip().capitalize()#strip - elimina spatiile/capitalize - intotdeauna prima litera este mare
KeyboardInterrupt
>>> L=[1,5,2,6,2,9]
>>> del L[0]
>>> l
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> l
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
[5, 2, 6, 2, 9]
>>> L.remove(5,2)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    L.remove(5,2)
TypeError: list.remove() takes exactly one argument (2 given)
>>> L.remove(1)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    L.remove(1)
ValueError: list.remove(x): x not in list
>>> L.remove(2)
>>> l
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l
NameError: name 'l' is not defined
>>> L
[5, 6, 2, 9]
>>> 
>>> example = ["A","B","C","A","B","D","A"]
>>> example.remove(A,B)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    example.remove(A,B)
NameError: name 'A' is not defined
>>> example.remove("A","C")
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    example.remove("A","C")
TypeError: list.remove() takes exactly one argument (2 given)
>>> example.remove("A")
>>> example
['B', 'C', 'A', 'B', 'D', 'A']
>>> example = ["A","B","C","A","B","D","A"]
>>> del example[3]
>>> example
['A', 'B', 'C', 'B', 'D', 'A']
>>> example = ["A","B","C","A","B","D","A"]
>>> del example[0:2]
>>> example
['C', 'A', 'B', 'D', 'A']
>>> 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
8
Hi! My name is Travis
What is your name?: Adrian
Hi! My name is Travis
What is your name?: 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
Hi! My name is Travis
What is your name?: Adi
Hi! My name is Travis
What is your name?: Dan
Hello Dan!
Would you like to be remove from the system (y/n)?: n
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/Python bible/travis.py", line 9, in <module>
    remove = input("Would you like to be remove from the system (y/n)?: ").strip.lower()   #lower - litere mici
AttributeError: 'builtin_function_or_method' object has no attribute 'lower'
>>> 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
Hi! My name is Travis
What is your name?: Dan
Hello Dan!
Would you like to be remove from the system (y/n)?: n
Hmmm I don't think I have meet you yet Dan
Would you like to be added to the system (y/n)?: y
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry', 'Dan']
Hi! My name is Travis
What is your name?: Dan
Hello Dan!
Would you like to be remove from the system (y/n)?: n
Hmmm I don't think I have meet you yet Dan
Would you like to be added to the system (y/n)?: y
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry', 'Dan']
['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry', 'Dan', 'Dan']
Hi! My name is Travis
What is your name?: 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
Hi! My name is Travis
What is your name?: 
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/Python bible/travis.py", line 5, in <module>
    name = input("What is your name?: ").strip().capitalize()  #strip - elimina spatiile/capitalize - intotdeauna prima litera este mare
KeyboardInterrupt
>>> 
>>> 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
Hi! My name is Travis
What is your name?: Adi
Hi! My name is Travis
What is your name?: 
======================== RESTART: C:/Users/Administrator/Desktop/Python bible/travis.py =======================
Hi! My name is Travis
What is your name?: Adrian
Hmmm I don't think I have meet you yet Adrian
Would you like to be added to the system (y/n)?: y
Hi! My name is Travis
What is your name?: adrian
Hello Adrian!
Would you like to be remove from the system (y/n)?: y
Hi! My name is Travis
What is your name?: adrian
Hmmm I don't think I have meet you yet Adrian
Would you like to be added to the system (y/n)?: n
No worries, see you around!
Hi! My name is Travis
What is your name?: 
Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/Python bible/travis.py", line 5, in <module>
    name = input("What is your name?: ").strip().capitalize()  #strip - elimina spatiile/capitalize - intotdeauna prima litera este mare
KeyboardInterrupt
>>> A = [5.2,12,72,55,88.0]
>>> A = A +[1]
>>> a
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> A
[5.2, 12, 72, 55, 88.0, 1]
>>> A = A +"BCD"
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    A = A +"BCD"
TypeError: can only concatenate list (not "str") to list
>>> A=A+["BCD"]
>>> a
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> A
[5.2, 12, 72, 55, 88.0, 1, 'BCD']
>>> A = A + list("BCD")
>>> A
[5.2, 12, 72, 55, 88.0, 1, 'BCD', 'B', 'C', 'D']
>>> A=A+list(123)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    A=A+list(123)
TypeError: 'int' object is not iterable
>>> A = A +list(str(123))
>>> A
[5.2, 12, 72, 55, 88.0, 1, 'BCD', 'B', 'C', 'D', '1', '2', '3']
>>> A = [5.2,12,72,55,88.0]
>>> A
[5.2, 12, 72, 55, 88.0]
>>> A=A+[5,6,7,5,8]
>>> A
[5.2, 12, 72, 55, 88.0, 5, 6, 7, 5, 8]
>>> A=A+[[5,6,7,5,8]]
>>> A
[5.2, 12, 72, 55, 88.0, 5, 6, 7, 5, 8, [5, 6, 7, 5, 8]]
>>> A[-1]
[5, 6, 7, 5, 8]
>>> A.append([10,11,12,13])
>>> A
[5.2, 12, 72, 55, 88.0, 5, 6, 7, 5, 8, [5, 6, 7, 5, 8], [10, 11, 12, 13]]
>>> A=A+[5,6,7,5,8]A = [5.2,12,72,55,88.0]A = [5.2,12,72,55,88.0]
SyntaxError: invalid syntax
>>> A = [5.2,12,72,55,88.0]
>>> A=A.append(10)
>>> A
>>> type(A)
<class 'NoneType'>
>>> A=[]
>>> type(A.append(10))
<class 'NoneType'>
>>> A = [5.2,12,72,55,88.0]
>>> 
>>> a
>>> A
[5.2, 12, 72, 55, 88.0]
>>> A.insert(2,100)
>>> A
[5.2, 12, 100, 72, 55, 88.0]
>>> A.insert(2,[100,120,1250])
>>> A
[5.2, 12, [100, 120, 1250], 100, 72, 55, 88.0]
>>> A = A.insert(2,60)
>>> A
>>> s="1,2,3"
>>> s[0]=3
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s[0]=3
TypeError: 'str' object does not support item assignment
>>> A=[1,2,3]
>>> A[0]=123
>>> A
[123, 2, 3]
>>> A=A.append(5)
>>> A=A.append(5)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    A=A.append(5)
AttributeError: 'NoneType' object has no attribute 'append'
>>> A=A.append(5)A=[1,2,3]
SyntaxError: invalid syntax
>>> 