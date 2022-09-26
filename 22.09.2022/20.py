a = {'123 123': 20, 'qwe qwe': 15, 'asd ads': 31, 'dfg dfg': 12}
print(list(map(lambda x: x.split()[0], filter(lambda x: a[x] >= 18, a.keys()))))
print([k.split()[0] for k, v in a.items() if v >= 18])
