# coding=utf-8
week = ['一', '二', '三', '四', '五', '六', '七']

for (index, v) in enumerate(week):
    print v + ' is ' + str(index)


def treatment(pos, el):
    return "%d: %s" % (pos, el)


seq = ["aa", "bb", "cc"]

print [treatment(i, el) for i, el in enumerate(week)]

cb = lambda i, ele: "%d:%s" % (i, ele)

print [cb(i, ele) for i, ele in enumerate(week)]
