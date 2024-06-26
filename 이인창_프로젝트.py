text = input('글자수를 셀 글:')
soword = 0
sxword = 0
sen = 0
for i in range(0,len(text),1):
    soword += 1
print('공백 포함 글자수: ')
print(soword)
for i in range(0,len(text),1):
    if text[i] == ' ':
        sxword += 0
    else:
        sxword += 1
print('공백 제외 글자수: ')
print(sxword)
for i in range(0,len(text),1):
    if text[i] == '.' or text[i] == '?' or text[i] == '!':
        sen += 1
    else:
        sen += 0
print('문장수 : ')
print(sen)
