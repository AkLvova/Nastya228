def prostoe (d) :
  # d - делитель числа N
  
  if d > last_d :
    return 0
  
  if N % d == 0 :
    return 1
  else :
    return prostoe (d + 1)
 
N = int (input ())
 
last_d = int (N ** 0.5)
# делители, равные 1 и N не проверяем
d = 2
 
if N == 1 :
  print ('NO')
elif prostoe (d) == 0 :
  print ('YES')
else :
  print ('NO')
