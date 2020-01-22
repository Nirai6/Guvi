wtf = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1, 2, 3]}}}}}
print(wtf[2][0])
print(wtf[2])
print(wtf['a'],wtf['a']['b'],wtf['a']['b']['c'],wtf['a']['b']['c']['d'],wtf['a']['b']['c']['d']['e'])
c=len(wtf['a']['b']['c']['d']['e'])
a=0
for i in range(0,c):
    a=((wtf['a']['b']['c']['d']['e'][i])+a)
print(a)
wtf['a']['b']['c']['d']['e']=['Chera','Chola','Pandiya']
print(wtf['a']['b']['c']['d']['e'])