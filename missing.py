arr=[1,4,2,5,6,7]
n=len(arr)+1

for j in range(1,n+1):
    if j in arr:
        continue
    else:
        print("missing number: ", j)
        break
