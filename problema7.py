S=str(input("Sa se introduca sirul de caractere: "))
#punctul a
print(S.count("A"))
#punctul b
a=S.replace("A","*")
print(a)
#punctul c
b=S.replace("B"," ")
print(b)
#punctul d
print(S.count("MA"))
#punctul e
c=S.replace("MA","TA")
print(c)
#punctul f
d=S.replace("TO"," ")
print(d)
#punctul g
e=S[::-1]
print(e)