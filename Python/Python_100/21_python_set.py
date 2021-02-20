#how to make set

a = {1, 2, 3, 4, 5}
b = {}
c = set('python')
d = set(range(5))
e = set()

'''
1) a = {1, 2, 3, 4, 5} => Set
2) b = {} => Dict
3) c = set('python') => Set
4) d = set(range(5)) => Set
5) e = set() => Set
'''

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# <class 'set'>
# <class 'dict'>
# <class 'set'>
# <class 'set'>
# <class 'set'>

print(a)
print(b)
print(c)
print(d)
print(e)

# {1, 2, 3, 4, 5}
# {}
# {'y', 'p', 'h', 'o', 't', 'n'}
# {0, 1, 2, 3, 4}
# set()
