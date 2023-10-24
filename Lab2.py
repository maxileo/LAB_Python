# EX 1
#def returnFib(n):
#    a = 1
#    b = 1
#    if n == 0:
#        return []
#    elif n == 1:
#        return [1]
#    elif n == 2:
#        return [1, 1]
#    fib = [1, 1]
#    for i in range(2, n):
#        c = a + b
#        fib.append(c)
#        a = b
#        b = c
#    return fib
#
#print(returnFib(5))

# EX 2
#import math
#
#def checkPrime(x):
#    if x == 2:
#        return True
#    elif x == 1:
#        return False
#    sqrtX = int(math.sqrt(x)) + 1
#    for d in range(2, sqrtX):
#        if x % d == 0:
#            return False
#    return True
#
#def getPrimeNumbers(nrs):
#    primeNrs = []
#    for nr in nrs:
#        if checkPrime(nr):
#            primeNrs.append(nr)
#    return primeNrs
#
#print(getPrimeNumbers([1, 2, 5, 25, 36, 78, 11, 13]))

# EX 3
import copy

def listsOperation(a, b, operationType):
    if operationType == "intersect":
        c = []
        for x in a:
            if x in b:
                c.append(x)
        return c
    if operationType == "reunite":
        c = []
        for x in a:
            if x not in c:
                c.append(x)
        for x in b:
            if x not in c:
                c.append(x)
        return c
    if operationType == "minus second":
        c = []
        for x in a:
            if x not in b:
                c.append(x)
        return c
    if operationType == "minus first":
        c = []
        for x in b:
            if x not in a:
                c.append(x)
        return c 
#def listsOperation(a, b, operationType):
#    a = set(a)
#    b = set(b)
#    if operationType == "intersect":
#        return list(a.intersection(b))
#    if operationType == "reunite":
#        return list(a.union(b))
#    if operationType == "minus second":
#        return list(a.difference(b))
#    if operationType == "minus first":
#        return list(b.difference(a))
#
a = [2, 3, 5, 8, 10, 12, 15, 15]
b = [2, 4, 5, 8, 11, 12, 12, 36]
print(listsOperation(a, b, "intersect"))
print(listsOperation(a, b, "reunite"))
print(listsOperation(a, b, "minus second"))
print(listsOperation(a, b, "minus first"))

# EX 4
#def compose(notes, moves, start):
#    composition = []
#    composition.append(notes[start])
#    for move in moves:
#        start = start + move
#        if start < 0:
#            start = len(notes) + start
#        if start >= len(notes):
#            start = start - len(notes)
#        composition.append(notes[start])
#    return composition
#
#print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

# EX 5
#def changeDiagonal(a):
#    for i in range(len(a[0])):
#        for j in range(i):
#            a[i][j] = 0
#    return a
#
#print(changeDiagonal([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))

# EX 6
#from collections import defaultdict
#
#def itemsLists(x, *argv):
#    itemsList = []
#    itemsFreq = defaultdict(int)
#    for list in argv:
#        for item in list:
#            itemsFreq[item] += 1
#    for item in itemsFreq:
#        if itemsFreq[item] == x:
#            itemsList.append(item)
#    return itemsList
#
#print(itemsLists(2, [1,2,3], [2,3,4],[4,5,6], [4,1, "test"]))

# EX 7
#def checkPalindrome(nr):
#    nrStringNormal = str(nr)
#    nrStringReversed = ''
#    lenStr = len(nrStringNormal)
#    for i in range(lenStr, 0, -1):
#        nrStringReversed = nrStringReversed + nrStringNormal[i-1:i]
#    return nrStringNormal == nrStringReversed
#
#def processPalindromes(nrs):
#    palindromes = [nr for nr in nrs if checkPalindrome(nr)]
#    return (len(palindromes), max(palindromes))
#
#print(processPalindromes([12321, 232, 45, 56, 787]))

# EX 8
#def asciiDiv(x=1, strs=[], flag = True):
#    print(x, flag)
#    result = []
#    for s in strs:
#        sChars = []
#        for c in s:
#            if flag and ord(c) % x == 0:
#                sChars.append(c)
#            if (not flag) and ord(c) % x != 0:
#                sChars.append(c)
#        result.append(sChars)
#    return result
#
#x = 2
#flag = False
#print(asciiDiv(x, ["test", "hello", "lab002"], flag))

# EX 9
#def getSpectators(sp):
#    spectators = []
#    for j in range(len(sp[0])):
#        for i in range(len(sp)-1, 0, -1):
#            current = sp[i][j]
#            for k in range(i-1, 0, -1):
#                if sp[k][j] >= current:
#                    spectators.append((i, j))
#    return spectators
#
#sp = [
# [1, 2, 3, 2, 1, 1],
# [2, 4, 4, 3, 7, 2],
# [5, 5, 2, 5, 6, 4],
# [6, 6, 7, 6, 7, 5]] 
#
#print(getSpectators(sp))

# EX 10
#def processLists(*argv):
#    result = []
#    maxLength = max ([len(x) for x in argv])
#    for i in range(maxLength):
#        elements = ()
#        for a in argv:
#            if i < len(a):
#                elements = elements + (a[i],)
#            else:
#                elements = elements + (None,)
#        result.append(elements)
#
#    return result
#
#print(processLists([1,2,3], [5,6,7,8], ["a", "b", "c", "d", "e"]))

# EX 11
#def customSort(tupleElem):
#    if len(tupleElem[1]) >= 3:
#        return tupleElem[1][2]
#    else:
#        return ''
#    
#tuples = [('abc', 'bcd'), ('abc', 'zza'), ('abc', 'abc')]
#sortedTuples = sorted(tuples, key=customSort)
#print(sortedTuples)

# EX 12
#from collections import defaultdict
#
#def groupRhyme(words):
#    result = []
#    rhymes = defaultdict(list)
#    for word in words:
#        rhymes[word[-2:]].append(word)
#    for rhyme in rhymes:
#        result.append(rhymes[rhyme])
#    return result
#
#print(groupRhyme(['ana', 'banana', 'carte', 'arme', 'parte', 'slanina']))
