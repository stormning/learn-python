s1 = set("qiwsir")
print s1

s2 = set([123, "google", "face", "book", "facebook", "book"])

print s2

s1 = set(['q', 'i', 's', 'r', 'w'])

lst = list(s1)

print lst

s1.add("x")

print s1

b_set = set("python")

print b_set

b_set.add("qiwsir")

print b_set

b_set.update({"c", "D"})

print b_set

print b_set.pop()

b_set.discard("D")

print b_set

b_set.clear()

print b_set

f_set = frozenset("qiwisir")
print f_set

a = {'q', 'i', 's', 'r', 'w'}

b = {'a', 'q', 'i', 'l', 'o'}

print a.difference(b)

print b.difference(a)

print a.issubset(b)

print a.issubset(b)

print a.union(b)

print a & b

print a.intersection(b)

