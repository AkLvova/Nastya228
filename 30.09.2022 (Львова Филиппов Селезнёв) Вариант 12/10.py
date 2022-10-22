names = ['Маша', 'Петя', 'Вася']
secret_names = list(map(lambda x: hash(x), names))
print(secret_names)
