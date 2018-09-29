from collections import defaultdict

mylist=[]


s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
d.default_factory
#<type 'list'>
for k, v in s:
   d[k].append(v)
print d.items()
#[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
print d
#defaultdict(<type 'list'>, {'blue': [2, 4], 'red': [1], 'yellow': [1, 3]})