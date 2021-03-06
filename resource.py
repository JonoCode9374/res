import sys # Used for argument parsing

# resource.py
# Description: the main interpreter

# Description: defines a function
# that reverses the keys on the keyboard horizontally.

# I don't see how this can be used; however, I am preserving this function for later potential uses.
def lshf(c): # one-character keyboard left shift.
    lut = '`1234567890-=\tqwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? \n'
    res = '=`1234567890-\\\tqwertyuiop[]\'asdfghjkl;/zxcvbnm,.+~!@#$%^&*()_|QWERTYUIOP{}"ASDFGHJKL:?ZXCVBNM<> \n'
    return res[lut.index(c)]

def krev(c): # One-character keyboard reversion. Carefully re-considered to make sure that it works in a wide variety of challenges.
    lut = '~!@#$%^&*()_+\tQWERTYUIOP{}|ASDFGHJKL:"\nZXCVBNM<>?` =123456789-0qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
    res = '+_)(*&^%$#@!~|}{POIUYTREWQ\t\n":LKJHGFDSA`?><MNBVCXZ-0987654321 \\=][poiuytrewq\';lkjhgfdsa/.,mnbvcxz'
    # TODO: Define a LUT that converts characters according
    # to my QWERTY keyboard of my laptop.
    return res[lut.index(c)]

try:
    file = open(sys.argv[1]) # Read a file
    cod = file.read() # And take contents.
except:
    cod = input()

code=[] # simple instruction splitter
for i in cod:
    code.append(i)

i = 0 # The program cursor
queue = [] # and the queue
rs=0 # Should the next characters be keyboard-reversed?
ret = [] # The previous states of the queue

while i < len(code): # The iteration starts now.

    s = code[i]
    #print("before:", s, queue)

    if rs:
        s=krev(s)

    if s=='\\': # Escaping instruction.
        i+=1
        try:
            queue.insert(0,code[i])
        except:
            queue.insert(0,'\n')

    # Usage: This escapes the next character in 
    # the source code in order to allow it to be
    # pushed onto the queue.    
    # Example: \# pushes # onto the queue.
    # If used on end of file, this pushes
    # a newline onto the queue.

    elif s == '<': # Rollback duplicate instruction.
        queue.insert(0,queue[-1])
    
    elif s == '>': # Queue rollback instruction.
        queue.insert(0,queue[-1])
        del queue[-1]

    # Usage: This copies the frontmost 
    # item of the queue to the back of 
    # the queue.
    # Example: ab< does aba onto 
    # the queue.
    
    elif s == '~': # Reverse the whole queue.
        queue=queue[::-1]
    
    # Usage: this reverses the whole queue's data.
    # Example: asdf~ will result in fdsa.

    elif s == '@' or s == ')' or s == '\t' or s == '|':
        # Easy, just keyboard reversing. (4 aliases for this instruction.)
        # Of course a tab is also key reversing (if you are desparately wanting space)
        rs=not rs

    elif s == '=': # Check equality between queue and previous state
        queue=[chr(queue==ret[-1][::-1])]

    elif s in '+-*/%^': # Operation of items *in* queue (rarely useful tho)
        if s=='^':s='**'
        exec("queue.insert(0,ord(queue.pop())"+s+"ord(queue.pop()))")
        if queue[0]>-1:
            queue[0]=chr(queue[0])

    elif s in ':;': # Greater than / less than
        pass
    
    else: # Boring push-onto-queue.
        queue.insert(0,s)

    # Usage: Just type it and it will be 
    # automatically on the queue!
    # Example: Hello, world!
    # This simply pushes the string onto the queue.

    ret.append(queue)

    i+=1
    #print("after:", s, queue)


# Just used for debugging, will be
# indicated by a flag later:
print(queue,ret,file=sys.stderr) # Print to STDERR for debugging the code.

# Implicit output
for _ in range(len(queue)):
    a=queue[0] # If the last item on the queue
    try:
        if ord(a) > 31 and ord(a) < 128 or ord(a)==10: # is printable:
            print(a,end="")# then print its charater code.
        else: # Otherwise,
            print(ord(a),end="") # print its ord code.
    except:
        print(a,end="") # Otherwise it is a negative number, treated uniquely.
    del queue[0]
