Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def about(name,age,likes):
	sentence = 'Meet {}! They are {} years old and they like {}'.format(name,age,likes)
	return sentence

>>> about('Jack',23,'Python')
'Meet Jack! They are 23 years old and they like Python'
>>> about(age=23, name='Jack',likes='Python')
'Meet Jack! They are 23 years old and they like Python'
>>> def about(name,age,likes='Python'):
	sentence = 'Meet {}! They are {} years old and they like {}'.format(name,age,likes)
	return sentence

>>> about('Jack',23)
'Meet Jack! They are 23 years old and they like Python'
>>> about('Jack',23,'Football')
'Meet Jack! They are 23 years old and they like Football'
>>> 