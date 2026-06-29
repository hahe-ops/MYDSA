arr = [1,3,4,0,4]
n = len(arr)
for i in range(n-2):
    for j in range(i+1, n-1):
        s1 = sum(arr[:i+1])
        s2 = sum(arr[i+1:j+1])
        s3 = sum(arr[j+1:])

        if s1 == s2 == s3:
            print(i, j)
            break
