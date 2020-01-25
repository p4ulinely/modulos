def tokenize(frase):
    # import string
    proibido = ['.', ',', '?', '!']

    # for char in string.punctuation:
    for char in proibido:
        frase = frase.replace(char, '')

    return frase.split(' ')

def countTokens(token, arr):
    count = 0
    for i in arr:
        if (i == token):
            count += 1
    
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

    return wordsFrequency

str = "aff... tô cansado e com fome ok?! minha gente, são da minha face com esse aff. \n minha mão está doendo e minha face tbm"

print(wordsFrequency(str))
