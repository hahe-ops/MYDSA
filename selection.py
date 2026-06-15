ar=[3,90,8,12,4]
n=len(ar)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if ar[j]<ar[min]:
            min=j
    print(ar)
    ar[i], ar[min] = ar[min], ar[i]

print(ar)
