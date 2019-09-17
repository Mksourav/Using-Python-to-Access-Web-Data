import re
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('\S+?@\S+', x)
print(y)

x='From: USing the : character'
y=re.findall('^F.+:',x)   #Greedymaching
print(y)
y=re.findall('^F.+?:',x)   #Non-Greedymaching
print(y)
