# dict 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
lux1['mana_regen'] = 228
print(lux1)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
x.setdefault('f', 100)
print(x)

x.update(a = 90)
print(x)

x.pop('a')
print(x)

print(x.items())
print(x.keys())
print(x.values())