fo=open("a_example.in", "r")
lines=[]
for line in fo.readlines():
    lines.append(line)

# data decleration
# line 1
a=lines[0]
a=a.split(' ')
max=int(a[0])
type=int(a[1])

# Line 2
b=lines[1]
b=b.split(' ')
slcs=[]
for i in b:
    slcs.append(int(i))

ordrd= slcs.copy()
ordrd.reverse()
maxi=0
cnt=[]
s=''
for i in ordrd:
    temp=maxi+i
    if temp<=max:
        maxi=temp
        if i not in cnt:
            cnt.append(i)

cnt.reverse()
print(len(cnt))
for j in cnt:
    s=s+str(len(slcs)-ordrd.index(j)-1)+' '
print(s)

wfile=open('a_example.txt','w')
wfile.write(f'{len(cnt)}\n')
wfile.write(s)
wfile.close()
