# resource.py
# Description: the main interpreter

# Description: defines a function
# that reverses the keys on the keyboard horizontally.
def krev(c): # One-character keyboard reversion.
    lut = '~!@#$%^&*()_+\tQWERTYUIOP{}|ASDFGHJKL:"\nZXCVBNM<>? `1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'
    res = '\t+_)(*&^%$#@!~|}{POIUYTREWQ\n":LKJHGFDSA ?><MNBVCXZ=-0987654321`\\][poiuytrewq\';lkjhgfdsa/.,mnbvcxz'
    # TODO: Define a LUT that converts characters according
    # to my QWERTY keyboard of my laptop.
    return res[lut.index(c)]

import sys # Used for argument parsing

try:
    file = open(sys.argv[1]) # Read a file
    code = file.read() # And take contents.
except:
    code = input()

i = 0 # The program cursor
queue = [] # and the queue
rs=0 # Should the next characters be keyboard-reversed?

while i < len(code): # The iteration starts now.
    
    s = code[i]

    if rs:
        s=krev(s)

    if s=='\\': # Escaping instruction.
        i+=1
        try:
            queue.insert(0,s)
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
    
    # Usage: This copies the frontmost 
    # item of the queue to the back of 
    # the queue.
    # Example: ab< does bab onto 
    # the queue.
    
    elif s == '~': # Reverse the whole queue.
        queue=queue[::-1]
    
    # Usage: this reverses the whole queue's data.
    # Example: asdf~ will result in fdsa.

    elif s == '@': # Easy, just keyboard reversing.
        rs=not rs
    
    else: # Boring push-onto-queue.
        queue.insert(0,s)

    # Usage: Just type it and it will be 
    # automatically on the queue!
    # Example: Hello, world!
    # This simply pushes the string onto the queue.

    i+=1

# Just used for debugging, will be
# indicated by a flag later:
print(queue)

queue=queue[::-1]

# Implicit output
for _ in range(len(queue)):
    a=queue.pop() # If the last item on the queue
    if ord(a) > 31 and ord(a) < 128 or ord(a)==10: # is printable:
        print(a,end="")# then print its charater code.
    else: # Otherwise,
        print(ord(a),end="") # print its ord code.