# coding=utf-8
t = 1, "23", [123, "abc"], ("learn", "python")

print t[3]

print t[1:]

for i in t:
    print i

print t[2][0]


# tuple比list更快
# tuple不可写，如果需要保护，则用tuple
# tuple可以在dict中被用作key
# tuples可以用在字符串格式化中