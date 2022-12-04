def foo(*args):# type: ignore
    print(*args)
    print(args)
    for a in args:
        print(a)

foo(1)
# 1

foo(1,2,3)
# 1
# 2
# 3

#----------------------------------

def bar(**kwargs):
    for a in kwargs:
        print(a, kwargs[a])
        
bar(name = 'one', age = 27)

#----------------------------------

def foos(a, b, c):
    print(a, b, c)

obj = {'b':10, 'c':'lee'}

foos(100,**obj)
# 100 10 lee

#-----------------------------------

def foo(bar, lee):
    print(bar, lee)

l = [1,2]

foo(*l)
# 1 2

#-------------------------------------

first, *rest = [1,2,3,4]
first, *l, last = [1,2,3,4]

#-------------------------------------

def func(arg1, arg2, arg3, *, kwarg1, kwarg2):
    pass

#-------------------------------------
"""
>>> x = [1, 2]
>>> [*x]
[1, 2]
>>> [*x, 3, 4]
[1, 2, 3, 4]

>>> x = {1:1, 2:2}
>>> x
{1: 1, 2: 2}
>>> {**x, 3:3, 4:4}
{1: 1, 2: 2, 3: 3, 4: 4}
"""

#-------------------------------------