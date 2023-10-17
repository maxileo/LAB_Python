# EX 1
#nrOfWords = int(input())
#
#def findCommonDivisor(a, b):
#    while b > 0:
#        aux = b
#        b = a % b
#        a = aux
#    return a
#
#for i in range(nrOfWords):
#    newNumber = int(input())
#    if i == 0:
#        commonDivisor = newNumber
#    else:
#        commonDivisor = findCommonDivisor(commonDivisor, newNumber)
#
#print(f"Cel mai mare divizor comun: {commonDivisor}")

# EX 2
#def findVowelsInString(s):
#    nrVowels = 0
#    s = s.lower()
#    for character in s:
#        if character in "aeiou":
#            nrVowels = nrVowels + 1
#    return nrVowels
#
#print(findVowelsInString("Bla bla asta e un string cu 11 vocale"))

# EX 3
#def findOccurencesStringInString(strToSearch, strToBeSearched):
#    lastFound = strToBeSearched.find(strToSearch)
#    nrFound = 1
#    while lastFound != -1:
#        lastFound = strToBeSearched.find(strToSearch, lastFound + 1)
#        nrFound = nrFound + 1
#    return nrFound - 1
#
#print(findOccurencesStringInString("string", "string Asta e un string care contine cuvantul string de 4 ori. string"))

# EX 4
#def convertToUnderscoreLowercase(strCamelCase):
#    for character in range(ord('A'), ord('Z')):
#        strCamelCase = strCamelCase.replace(chr(character), f"_{chr(character - ord('A') + ord('a'))}")
#    return strCamelCase[1:]
#
#print(convertToUnderscoreLowercase("UpperCamelCase"))

# EX 5
#n = 4
#m = 4
#matrix = [['f', 'i', 'r', 's'], ['n', ' ', 'l', 't'], ['o', 'b', 'a', ' '], ['h', 't', 'y', 'p']]
#matrixVisited = []
#for i in range(n):
#    arr = [0]*m
#    matrixVisited.append(arr)
#
#stringCreated = ''
#directions = {}
#directions["right"] = [0, 1]
#directions["down"] = [1, 0]
#directions["left"] = [0, -1]
#directions["up"] = [-1, 0]
#
#nextDirection = {}
#nextDirection["right"] = "down"
#nextDirection["down"] = "left"
#nextDirection["left"] = "up"
#nextDirection["up"] = "right"
#
#currentDirection = "right"
#pozI = 0
#pozJ = 0
#blocked = False
#while not blocked:
#    matrixVisited[pozI][pozJ] = 1
#    stringCreated = stringCreated + matrix[pozI][pozJ]
#    nextI = directions[currentDirection][0]
#    nextJ = directions[currentDirection][1]
#    if (pozI + nextI >= n or pozI + nextI < 0) or (pozJ + nextJ >= m or pozJ + nextJ < 0) or matrixVisited[pozI + nextI][pozJ + nextJ] == 1:
#        currentDirection = nextDirection[currentDirection]
#        if matrixVisited[pozI + directions[currentDirection][0]][pozJ + directions[currentDirection][1]] == 1:
#            blocked = True
#    pozI = pozI + directions[currentDirection][0]
#    pozJ = pozJ + directions[currentDirection][1]
#
#print(stringCreated)

# EX 6
#def checkPalindrome(nr):
#    nrStringNormal = str(nr)
#    nrStringReversed = ''
#    lenStr = len(nrStringNormal)
#    for i in range(lenStr, 0, -1):
#        nrStringReversed = nrStringReversed + nrStringNormal[i-1:i]
#    return nrStringNormal == nrStringReversed
#
#print(checkPalindrome(23532))

# EX 7
#def extractFirstNr(strNr):
#    nrFoundStr = ""
#    startedNr = False
#    for character in strNr:
#        if character in "1234567890":
#            startedNr = True
#            nrFoundStr = nrFoundStr + character
#        else:
#            if startedNr:
#                break
#
#    return int(nrFoundStr)
#
#print(extractFirstNr("abc123abc"))

# EX 8
#def countBits(nr):
#    nrBits = 0
#    for i in range(32):
#        if nr & ( 1 << i):
#            nrBits = nrBits + 1
#    return nrBits
#
#print(countBits(24))

# EX 9
#def findCommonLetter(s):
#    s = s.lower()
#    foundLetters = {}
#    for character in s:
#        if character != ' ':
#            if character in foundLetters:
#                foundLetters[character] = foundLetters[character] + 1
#            else:
#                foundLetters[character] = 1
#    
#    return max(foundLetters, key = lambda letter: foundLetters[letter])
#
#print(findCommonLetter("an Apple is not a tomAto"))


# EX 10
#def getNrWords(s):
#    return len(s.split())
#
#print(getNrWords("I have Python exam"))