#проект
sentence = 'Hello World abc 454'

context = sentence.split(' ')
full_text = []

for i in context:
    if len(i) >= 5:
        text = f"{i[::-1]} "
    else:
        text = f'{i} '

    full_text.append(text)
overall_text = ''.join(full_text)
print(f'Окончательный текст: {overall_text}')


#объяснение
sentence = '1,2,3,4,5,6,7,8,9,10'
sentence2 = 'a+b+c+d+g+e'
sentence3 = 'bahram&bahram2&bahram3'

context = sentence.split(',')
context2 = sentence2.split('+')
context3 = sentence3.split('&')

for i in range(0, 10):
    if i == 5:
        break

    print(f'{i}Hello')


text = 'hello'
list1 = ['h', 'e', 'l', 'l', 'o']

print(list1[::-1])

