a = []
print type(a)

a = [2, "123", 'asfg']

print a

print a[0]

print a[:2]

print a[-1]

print a[-2]

a.append("xx")

print a

a[len(a):] = ["yy"]

print a

print len(a)

a[5:] = ["zz"]

print a

a.insert(1, "333")

print a

b = [2, 'II']

a.extend(b)

print a

a.extend("666")

print a

a[len(a):] = ['77', '88']

print a

print a.count('6')

print a.pop(1)

print a

a.remove('6')

print '6' in a

if '6' in a:
    a.remove('6')
else:
    print a

print range(1, 9, 1)

test = [2, 31, 12, 4]

list.sort(test, lambda x, y: y - x)
print test
test.sort(reverse=True)
print test

print sorted(test, reverse=False)

line = 'hello.world.python'

print line.split('.', 1)

print "a".join(["dd", "cc"])
