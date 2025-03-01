
#print(text.index('llo'))


text = 'stol'
srch_substr = 'ol'
len_srch_substr  = len(srch_substr)
for i in range(len(text) - len(srch_substr)+1):
    if text[i: i + len_srch_substr] == srch_substr:
        print(i)
        break
else:
    print('такой подстроки в строке нет')


text = 'stol'
srch_substr = 'ol'
len_srch_substr  = len(srch_substr)
pos = 0
while text:
    if text[:len_srch_substr] == srch_substr:
        print(pos)
        break
    pos += 1
    text = text[1:]
else: print('такой подстроки не существует')












