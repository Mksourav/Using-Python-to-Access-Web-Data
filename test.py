#Regular Expression with File handling
import re
# fname=input("Enter the file name:")
fh=open('mbox-short.txt')
for line in fh:
    line=line.rstrip()
    # if line.find('From:')>=0:
    # if re.search('From:',line):
    # if line.startswith('From:'):
    # if re.search('^From:',line):
    if re.search('^From.*:',line):
        print(line)

print('Test')
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
