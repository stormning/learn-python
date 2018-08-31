# coding=utf-8
print "小明说:\"我没有烧圆明园\""
print '小明说:\"我没有烧圆明园\"'
a = 5
b = "hello world"
print str(a) + b

print "a" + "b"

c = "世界"
d = "学python"
e = c + d
print e
print "one is %d" % a
print "one is %s" % d
print "one is %d %s" % (a, d)

print len(c)
print d.upper()
print "abcd".capitalize()
print "Abcd".istitle()
for item in c:
    print item
