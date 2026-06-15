ar=[3,90,9,12,4]
n=len(ar)
for i in range(n-1):
    for j in range(n-i-1):
        if ar[j]>ar[j+1]:
            ar[j],ar[j+1]=ar[j+1],ar[j]
        else:
            continue
    print("after iteration: ", ar)

print("sorted array: ", ar)
