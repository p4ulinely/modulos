def tokenize(frase):

    # import string
    proibido = ['.', ',', '?', '!', '(', ')', '[', ']', '{', '}']
    temp = []

    # for char in string.punctuation:
    for char in proibido:
        frase = frase.replace(char, '')

    for e in frase.split(' '):
        if(e != ''): temp.append(e.lower())

    return temp

def countTokens(token, arr):
    count = 0
    for i in arr:
        if (i == token): count += 1
    
    return count

def wordsFrequency(text):
    distinct = set()
    tokensArray = []
    wordsFrequency = []

    for line in text.split('\n'):
        tokens = tokenize(line)
        distinct.update(tokens)
        tokensArray += tokens
    
    for token in distinct:
        qnt = countTokens(token, tokensArray)
        wordsFrequency.append([token, qnt])

    wordsFrequency.sort()

    return wordsFrequency

f = open("file.txt", "r")
print(wordsFrequency(f.read()))
