def rests(arg: int) -> list:
    return list(map(lambda x: x % arg, lst))
 
lst = [42, 17, 34, 100501]
print(*rests(3))
print(*lst)
