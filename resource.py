import sys # Used for argument parsing

try:
    file = open(sys.argv[1]) # Read a file
    code = file.read() # And take contents.
except:
    code = input()

i = 0 # The program cursor
queue = [] # and the queue

while i < len(code): # The iteration starts now.
    if code[i]=='\\': # Escaping instruction.
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

    elif code[i] == '<': # Rollback duplicate instruction.
        queue.insert(0,queue[-1])
    
    # Usage: This copies the frontmost 
    # item of the queue to the back of 
    # the queue.
    # Example: ab< does bab onto 
    # the queue.
    
    elif code[i] == '~': # Reverse the whole queue.
        queue=queue[::-1]
    
    # Usage: this reverses the whole queue's data.
    # Example: asdf~ will result in fdsa.

    else: # Boring push-onto-queue.
        queue.insert(0,code[i])

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
