
#text = 'proizvolnyi text'
text = input('Введите произвольный текст: ')
mydict = dict()
for i in text:
    if i == ' ':
        i = 'Пробел'
    if i in mydict.keys():
        mydict[i] = mydict[i] + 1
    else:
        mydict[i] = 1
print(mydict)

