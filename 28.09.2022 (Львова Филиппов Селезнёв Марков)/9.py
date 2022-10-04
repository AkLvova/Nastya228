n, f, s = map( int, input('n, f, s = ').split() )
k, rem = divmod(n-f, s)
print( ['Нет', 'Да'][ k >= 0 and not rem ] )
