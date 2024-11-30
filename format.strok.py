import random 
a=["Сегодня ", "на ", "улице ", "было ", "тепло ", "и ", "солнечно."]
b=[a.split()[random.randint(0,len(a.split())-1)] for a in a]

c=" ".join(b)
print(c)
