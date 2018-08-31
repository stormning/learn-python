mydict = {'name': 'storming', 'age': 16}
print mydict['age']

name = (["first", "Google"], ["second", "Yahoo"])

print dict(name)

print mydict.keys()

print mydict.values()

print mydict.items()

for k in mydict:
    print mydict[k]

print [mydict[k] for k in mydict]

print mydict.get("name")

mydict.pop("name")

print mydict

del mydict['age']

print mydict
