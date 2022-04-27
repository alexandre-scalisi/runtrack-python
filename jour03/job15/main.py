def check(word1, word2, index1, index2, wildcard):
    if index2 == len(word2) and wildcard or index1 == len(word1) and index2 == len(word2):
        return True
    if index2 == len(word2):
        return False
    if word2[index2] == '*':
        return check(word1, word2=word2, index1=index1, index2=index2 + 1, wildcard=True)
    if index1 == len(word1):
        return False
    if word1[index1] == word2[index2]:
        return check(word1, word2, index1 + 1, index2 + 1, wildcard=False)
    if word2[index2] != word1[index1] and wildcard:
        print('test')
        return check(word1=word1, word2=word2, index1=index1+1, index2=index2, wildcard=wildcard)
    return False


word1 = input('Entrer le premier mot ')
word2 = input('Entrer le deuxième mot ')

print(check(word1, word2, 0, 0, False))
