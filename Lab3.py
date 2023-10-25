# LAB 3

# EX 1
#def setsOperation(a, b, operationType):
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
#a = [2, 3, 5, 8, 10, 12, 15]
#b = [2, 4, 5, 8, 11, 12, 36]
#print(setsOperation(a, b, "intersect"))
#print(setsOperation(a, b, "reunite"))
#print(setsOperation(a, b, "minus second"))
#print(setsOperation(a, b, "minus first"))

# EX 2
#from collections import defaultdict
#
#def chDictionary(s):
#    chrs = defaultdict(int)
#    for c in s:
#        chrs[c] = chrs[c] + 1
#    return chrs
#
#print(chDictionary("Ana has apples."))

# EX 3

#def isType(a):
#    types = (dict, list, set, tuple)
#    return isinstance(a, types)
#
#def isDict(a):
#    return isinstance(a, dict)
#
#def checkDictionaries(a, b, rez):
#    if type(a) != type(b):
#        return 1
#    if isDict(a):
#        for x in a:
#            if isType(a[x]):
#                if x not in b:
#                    return 1
#                if isType([b[x]]):
#                    rez = rez + checkDictionaries(a[x], b[x], rez)
#                else:
#                    return 1
#            else:
#                if x not in a or x not in b:
#                    return 1
#                if a[x] != b[x]:
#                    return 1
#    else:
#        if len(a) != len(b):
#            return 1
#        for i in range(len(a)):
#            if isType(a[i]) and isType(b[i]):
#                rez = rez + checkDictionaries(a[i], b[i], rez)
#            else:
#                if a[i] != b[i]:
#                    return 1
#            
#    return rez
#
#def checkDictionariesBool(a, b):
#    return checkDictionaries(a, b, 0) == 0
#
#a = {}
#a[1] = 5
#a[2] = 7
#a["salut"] = 7
#a[3] = [1, 2, [1, 2, 3]]
#a[4] = {}
#a[4][1] = "1"
#a[4]["blabla"] = "2"
#
#b = {}
#b[1] = 5
#b[2] = 7
#b["salut"] = 7
#b[3] = [1, 2, [1, 2, 3]]
#b[4] = {}
#b[4][1] = "1"
#b[4]["blabla"] = "2"
#
#print(checkDictionariesBool(a, b))

# EX 4

#def buildXmlElement(tag, content, **kwargs):
#    xmlElem = f"<{tag}"
#    for key, value in kwargs.items():
#        xmlElem += f' {key}="{value}"'
#    
#    xmlElem += ">"
#    xmlElem += content
#    xmlElem += f"</{tag}>"
#
#    return xmlElem
#
#print(buildXmlElement("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))

# EX 5

#def isInSet(x, rules):
#    for rule in rules:
#        if x == rule[0]:
#            return True
#    return False
#
#def validateDict(a, rules):
#    for rule in rules:
#        if rule[0] in a:
#            if not a[rule[0]].startswith(rule[1]):
#                return False
#            if not a[rule[0]].endswith(rule[3]):
#                return False
#            if not rule[2] in a[rule[0]][1:-1]:
#                return False
#    for key in a:
#        if not isInSet(key, rules):
#            return False
#    return True
#
#rules={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} 
#d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
#print(validateDict(d, rules))


# EX 6
#def listStatistics(a):
#    b = set(a)
#    return (len(b), len(a) - len(b))

# EX 7
#def operations(*args):
#    rez = {}
#    for i in range(len(args)):
#        setBefore = args[i]
#        for j in range(i+1, len(args)):
#            reunionStr = f"{str(setBefore)} | {str(args[j])}"
#            intersectionStr = f"{str(setBefore)} & {str(args[j])}"
#            minusSecondStr = f"{str(setBefore)} - {str(args[j])}"
#            minusFirstStr = f"{str(args[j])} - {str(setBefore)}"
#
#            reunion = setBefore.union(args[j])
#            intersection = setBefore.intersection(args[j])
#            minusFirst = args[j].difference(setBefore)
#            minusSecond = setBefore.difference(args[j])
#
#            rez[reunionStr] = reunion
#            rez[intersectionStr] = intersection
#            rez[minusSecondStr] = minusSecond
#            rez[minusFirstStr] = minusFirst
#
#    return rez
#
#print(operations({1, 2}, {2, 3}, {3, 4}))

# EX 8
#from collections import defaultdict
#
#def loop(mapping):
#    rez = []
#    visited = defaultdict(int)
#    key = "start"
#    while visited[key] == 0:
#        visited[key] = 1
#        rez.append(mapping[key])
#        key = mapping[key]
#    return rez[:-1]
#
#print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

# EX 9
#def countArgs(*args, **kwargs):
#    count = 0
#    for arg in args:
#        if arg in kwargs.values():
#            count += 1
#    return count
#
#print(countArgs(1, 2, 3, 4, x=1, y=2, z=3, w=5))
