# Stacks
# stacks & ques are widely used elementary data structures!
# they are linear data structures (no nesting!) where the insert & delete options are pre specified!
# meaning that the way insertions & deletions are pewrformed on these data structures cannot be modified!

# consider stacks as a vertical container!
# placement of new elements takes place on top of the existing one!
# thus to remove the bottom most element, one has to remove all the elements above it!
# LIFO paradigm! Last In First Out!
# elements can only be placed one top of another
# and elements can only be removed from the top!

# conventions
# push - insert a new element at top
# pop - remove an existing element from the top

stack = list()

def push(stack, value):
    stack.append(value)

def pop(stack):
    return stack.pop()

push(stack, "Sarah")
push(stack, "Leslie")
push(stack, "Jessica")
push(stack,"Samantha")

stack

pop(stack)
stack

# in applications stacks are used to implement the UNDO function!
# where users are able to revert back to the previous state of the objects of their creation!

# can lists really be used as stacks?
# one can eccess elements at any existing index, modify them etc...

# Ques
# linear data structure; no nesting!
# FIFO paradigm: First In First Out
# predefined insertion & deletions i.e joining the que & leaving the que!
# one can only join at the end and leave from the front!

que = list()

def enque(que, value):
    que.append(value)
    return que

def deque(que):
    try:
        del que[0]
        # or que.pop(index)
        return que
    except:
        raise(IndexError("No member elements left to deque!"))

enque(que, "Sarah")  
enque(que, "John")
enque(que, "Pamela")
enque(que, "Jovanne")
enque(que, "Smithson")
enque(que, "Leslie")

deque(que)

# still this implementation is incorrect! lists are mutable, one can remove, modify elements at any indices
# ques are used in memory access & file reading
# supppose multiple workers need to access a memory, hard drives can only allow one thread at a time!
# thus hard drives keep a que of access requests made by applications and broker them accordingly!
# first requested, first gets access!