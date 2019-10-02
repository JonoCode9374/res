# res
Res can either be understanded as ([re]stricted [s]ource) or [r]estrictions [e]asily [s]implified. This language is designed to make restricted source challenges easy or even trivial. (Alternative name for challenges that do not relate to the language name length: Resource)

# Resources
* [Try It Online!](https://tio.run/#res)
* [Esolangs.org page(primarily drafts for the language. Please do not rely on this page for documentation and examples.)](https://esolangs.org/wiki/Resource)

# Reference
<!-- I figured I'd help out a little here. -->
<!-- If you are reading the comments here, you must fall under one of these three categories:
1) You are A-ee looking at the raw source of what I did (In which case, please leave comments in)
2) You are a stickybeak who has nothing better to do with their time than looking at raw markdown
or
3) You are like me and have absolutely no clue how queues work as you primarily work with stacks
For category 3, I shall leave helpful guides in the comments about how each operator would work if res used stacks.
However, a helpful hint is that the first item is the "front" and the last item is the "back"
~JonoCode9374/Jono2906
-->
## Rollback & Duplicate
The `<` command takes the front of the queue and copies it to the back of the queue.
<!-- Or, if you are a stack person, it right shifts the queue, duplicates, reverses and performs another right shift -->
Examples:

    [Prog]: ab<
    [Out]: aba
    
    [Prog]: ab<cd<
    [Out]: adcaba
    
## Escape
The `\` command deals with placing special characters (e.g. `<`, `@`) onto the queue
<!-- This is just how like Element (https://esolangs.org/wiki/Element) and Keg (https://esolangs.org/wiki/Keg) do things -->

Examples:

    [Prog]: \a
    [Out]: a
    
    [Prog]: \<\<
    [Out]: <<
 
## Reverse
The `~` command reverses the entire queue
<!-- Literally just reverses the theoretical stack us comment readers are imagining. However, the queue is, in a sense, already reversed, so this puts it into a stack-like order -->

Examples:

    [Prog]: abc~
    [Out]: abc
    
    [Prog]: Hello, World!~
    [Out]: Hello, World!

## Keyboard Shift --> "One-character keyboard reversion"
This is achieved by using either `@(|` or a tab (`\t`). It "reverses" the letters inputted from the keyboard so that letters can be easily avoided.

_N.B. The unreversed keyboard mapping is: '\~!@#$%^&*()\_+\tQWERTYUIOP{}|ASDFGHJKL:"\nZXCVBNM<>?\` =123456789-0qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./'_

_The reversed keboard mapping is: +\_)(*&^%$#@!\~|}{POIUYTREWQ\t\n":LKJHGFDSA\`?><MNBVCXZ-0987654321 \\=]\[poiuytrewq\';lkjhgfdsa/.,mnbvcxz_

<!-- This isn't really stack related, so there is no stack comparison -->

Examples:

    [Prog]: @abc@
    [Out]: ,n'
    
    [Prog]: @Hello, World!@~
    [Out]: ddtc-17{tpdl_
<!-- Yes, I know it looks messy, but that's the way things roll -->

## Queue Rollback
The `>` command takes the front of the queue and places it at the back.
<!-- For stacks, this is pretty much a right shift. Well, it _is_ a right shift-->

Examples:

    [Prog]: abc>
    [Out]: acb
    
    [Prog]: adb>>
    [Out]: dab
<!--          On them haters. xD lol, got'em -->

## Mathematical Operators
The commands `+-*/%^` all handle mathematical operations (add, subtract, multiply, divide, modulo and exponante respectively). It takes the first two items and applies the operation to them.
<!-- In the world of stacks, I would usually write this as pop a, b and push b <op> a -->

Examples:

    [Prog]: AA+
    [Out]: 130
    
    [Prog] AA+<A+
    [Out]: 260A

<!-- Comment readers, this is the end of the road for our little journey. Thanks for sticking around with me as I try to explain everything involved with res/resource/Resource/Res. See y'all soon\! (I don't know if exclamation marks work well in comments.) -->

    

  
