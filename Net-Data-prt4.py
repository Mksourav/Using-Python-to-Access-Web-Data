import urllib.request, urllib.parse, urllib.error

fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#fhand=urllib.request.urlopen('http://dr-chuck.com/page1.htm')

counts=dict()   

for line in fhand:
    words=line.decode().split()
    print(line.decode().strip())
    for word in words:
        counts[word]=counts.get(word, 0)+1
print("\nWord counts::",counts)

