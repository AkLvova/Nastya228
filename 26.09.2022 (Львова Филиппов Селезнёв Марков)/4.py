def task(arr,l,r):
    p=1
    s=0
    for a in arr[l:r+1]:
        s=s+a*p
        p=-p
        return s
