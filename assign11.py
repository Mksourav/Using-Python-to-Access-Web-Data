import re
fn=("regex_sum_242047.txt")
fh=open(fn)
sum=0
for line in fh:
    line=re.findall('[0-9]+', line)
    for i in line:
        i=int(i)
        sum=sum+i
print(sum)
    # print(line)
