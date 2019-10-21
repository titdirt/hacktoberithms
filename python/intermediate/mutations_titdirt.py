def checkMutation(wordList):
    word1 = []
    word2 = []
    for i in wordList[0]:
        word1.append(i.lower())
    for i in wordList[1]:
        word2.append(i.lower()) 
    for i in word2:
        if i not in word1:
            return False
        else:
            word1.remove(i)
    return True
