dicta = {'a': 10, 'b': 20}
dictb = {'b': 30, 'c': 40}

dictout = {}

for key in dicta:
    if key in dictb:
        dictout[key] = dicta[key] + dictb[key]
    else:
        dictout[key] = dicta[key]

for key in dictb:
    if key not in dicta:
        dictout[key] = dictb[key]

print(dictout)
