# coding=utf-8
for i in "hello":
    print i

for i in "hello":
    print i + ",",

print range(len("hello"))

result = []
for i in range(1, 100):
    if i % 3 == 0:
        result.append(i)

print result

squares = [x ** 2 for x in range(1, 10)]

print squares

test2 = [n for n in range(1, 100) if n % 3 == 0]

print test2

print range(3, 100, 3)

mybag = [' glass', 'apple  ', 'green leaf ']
print [n.strip() for n in mybag]

week = ['一', '二', '三', '四', '五', '六', '七']
for i in range(len(week)):
    print week[i] + ' is ' + str(i)
