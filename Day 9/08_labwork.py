# merge two dt
d1 = {'a': 50, 'b': 100}
d2 = {'x': 200, 'y': 100}
d = d1.copy()
d.update(d2)
print(d)