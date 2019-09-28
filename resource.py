import sys
file=open(sys.argv[1])
code=file.read()
i = 0
queue = []
while i < len(code):
    if code[i]=='#':
        try:
            while code[i]!='\n':
                i+=1
        except:
            continue
    else:
        queue.insert(0,code[i])
    i+=1
print(queue)
for _ in range(len(queue)):
    a=queue.pop()
    if ord(a) > 31 and ord(a) < 128 or ord(a)==10:
        print(a,end="")
    else:
        print(ord(a),end="")