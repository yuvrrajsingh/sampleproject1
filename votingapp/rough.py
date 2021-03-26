mydict1 = {
    'hello' : 2,
    'hyy' : 1,
    'singh' : 4,
}
d = {}

for  val in sorted(mydict1.values(), reverse=True):
    for key in mydict1.keys():
        if mydict1[key]==val:
            d[key]=val

print(d)