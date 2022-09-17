#get sentence from user

original= input('Tell me a sentence: ').strip().lower()

#split sentence into words

words = original.split()
print(words)


#loop through words and convert to pig latin

new_words = []

#if starts with vowels, just add "guit"

for word in words:
    if word[0] in 'aeiou':
        new_word = word +'guit'
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_positon = vowel_position+1
            else:
                break
        consonant = word[:vowel_position]
        the_rest = word[vowel_position:]

#Otherwise, move the first consonant cluser to the end, and add "groh"
        
        new_word = the_rest + consonant + 'groh' 
        new_words.append(new_word)



#stick words back together

output =' '.join(new_words)

#output the final string
print(output)
