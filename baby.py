from random import choice

questions = ['Why the Earth isn\'t flat?: ', 'Why the grass is green?: ', 'Why the world is spinning?: ']

question = choice(questions)
answer = input(question).strip().lower()

while answer!='just because':
    answer = input('why?:').strip().lower()

print('Oh...Okey...')

